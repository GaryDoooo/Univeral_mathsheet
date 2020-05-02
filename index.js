"use strict";

const socket = require("socket.io"), // socket for serving the chat service
    express = require("express"),
    path = require("path"),
    app = express(),
    server = require("http").Server(app),
    server_io = socket(server); // the io for chat server

/////// set the http listen and httpd working directory
app.set("view engine", "html")
    .get("/", function(req, res) {
        res.sendFile(path.join(__dirname + "/public/"));
    })
    .use(express.static(path.join(__dirname, "public")));

if (module === require.main) {
    const PORT = process.env.PORT || 8080;
    server.listen(PORT, () => {
        console.log(`App listening on port ${PORT}`);
        console.log("Press Ctrl+C to quit.");
    });
}

// try_js_py()
server_io.on("connection", function(socket) {
    console.log(`made socket connection ${socket.id}`, socket.id);

    socket.on("GetListHTML", function(cb_function) {
        console.log("received client get HTML request");
        try {
            var ps = require("python-shell");
            var options = {
                args: []
            };
            ps.PythonShell.run("./python_modules/getHTML_js_interface.py", options, function(
                err,
                results
            ) {
                if (err) {
                    console.log(err);
                    cb_function({
                        done: err
                    });
                } else {
                    console.log("get html list finished");
                    results = replace_latex_for_multiple__strings(results);
                    // console.log("Converted html list Latex to svg.");
                    // console.log(results);
                    cb_function({
                        done: true,
                        selection_list: results[0],
                        abstract_list: results[1]
                        // 'page_key': results[2]
                    });
                    // console.log(results['problem_list'])
                }
            });
        } catch (err) {
            cb_function({
                done: err
            });
            // TabNine::semSemantic completion enabled.
        }
    });

    socket.on("gen", function(
        problem_num,
        num_of_col,
        question_type_list_string,
        cb_function
    ) {
        console.log(
            "received client gen request",
            problem_num,
            num_of_col,
            question_type_list_string
        );
        try {
            var ps = require("python-shell");
            var options = {
                args: [
                    problem_num,
                    num_of_col,
                    question_type_list_string,
                    "There_is_no_page_key_input" // new means to generate new page key
                ]
            };
            ps.PythonShell.run("./python_modules/js_interface.py", options, function(
                err,
                results
            ) {
                if (err) {
                    console.log(err);
                    cb_function({
                        done: err
                    });
                } else {
                    // console.log(results);
                    // results = fix_python_backslash_error(results);
                    console.log("Get problem HTML from python code.");
                    results = replace_latex_for_multiple__strings(results);
                    // console.log("Converted latex to svg finished");
                    cb_function({
                        done: true,
                        problem_list: results[0],
                        answer_list: results[1]
                        // 'page_key': results[2]
                    });
                    // console.log(results['problem_list'])
                }
            });
        } catch (err) {
            cb_function({
                done: err
            });
            // TabNine::semSemantic completion enabled.
        }
    });

    socket.on("answer", function(problem_num, col_num, page_key, cb_function) {
        try {
            var ps = require("python-shell");
            var options = {
                args: [
                    problem_num,
                    col_num,
                    "dummyInput",
                    page_key // if page key not 'new' means to get answers back
                ]
            };
            ps.PythonShell.run("./python_modules/js_interface.py", options, function(
                err,
                results
            ) {
                if (err) {
                    console.log(err);
                    cb_function({
                        done: err
                    });
                } else {
                    console.log("finished");
                    // console.log(results);
                    // results = fix_python_backslash_error(results);
                    results = replace_latex_for_multiple__strings(results);
                    cb_function({
                        done: true,
                        problem_list: results[0],
                        answer_list: results[1]
                        // 'page_key': results[2]
                    });
                    // console.log(results['problem_list'])
                }
            });
        } catch (err) {
            cb_function({
                done: err
            });
        }
    });
}); /// end of io connect

// function fix_python_backslash_error(input_string) {
//     var replace_table = [
//         [String.raw `\\div`, String.raw `\div`]
//     ];
//     for (var i = 0; i < input_string.length; i++) {
//         for (var j = 0; j < replace_table.length; j++) {
//             input_string[i].replace(replace_table[j][0], replace_table[j][1]);
//         }
//     }
//     return input_string;
// }

// ////////////////////////////////////////////////////////////////
// // change latex in multiple strings
function replace_latex_for_multiple__strings(input_strings) {
    var number_of_strings = input_strings.length;
    var number_of_done = Array(number_of_strings).fill(0);
    var results = Array(number_of_strings).fill("");
    for (var i = 0; i < number_of_strings; i++) {
        replace_latex(input_strings[i], function(result) {
            results[i] = result;
            number_of_done[i] = 1;
        });
        // results[i] = input_strings[i].replace(/\//gi, "\\");
        // results[i] = results[i].replace("<latex>", "$$");
        // results[i] = results[i].replace("</latex>", "$$");
    }
    while (number_of_done.reduce((a, b) => a + b, 0) < number_of_strings) {
        var i = 1;
        i++; // use the while loop to wait all the results are ready
    }
    return results;
}
// ////////////////////////////////////////////////////////////////
// // Using MathJax to convert TeX into svg
// // Load MathJax 3 refer to https://github.com/mathjax/MathJax

function replace_latex(input_string, cb_function) {
    var latex_start_index = input_string.indexOf("<latex>");
    // console.log("latex_start_index", latex_start_index);
    if (latex_start_index == -1) {
        cb_function(input_string);
        // return input_string;
    } else {
        var prefix = input_string.substr(0, latex_start_index);
        var latex_end_index = input_string.indexOf("</latex>");
        var latex_length = latex_end_index - latex_start_index;
        var suffix = input_string.substr(
            latex_end_index + 8,
            input_string.length - (latex_end_index + 8)
        );
        var latex = input_string.substr(
            latex_start_index + 7,
            latex_end_index - (latex_start_index + 7)
        );
        // console.log("latex_end_index", latex_end_index);
        // console.log("latex_length", latex_length);
        // console.log("prefix=" + prefix);
        // console.log("suffix=" + suffix);
        // console.log("latex=" + latex);
        // console.log("Start to convert latex", latex.replace(/\//gi, "\\"));
        var svg_html = "$$" + latex.replace(/\//gi, "\\") + "$$";
        replace_latex(suffix, function(output) {
            cb_function(prefix + svg_html + output);
        });
    }
}
////// Use old version of mathjax node 2.1.1 
// var mjAPI = require("mathjax-node");
// mjAPI.config({
//     MathJax: {
//         // traditional MathJax configuration
//     }
// });
// mjAPI.start();

// function replace_latex(input_string, cb_function) {
//     var latex_start_index = input_string.indexOf("<latex>");
//     // console.log("latex_start_index", latex_start_index);
//     if (latex_start_index == -1) {
//         cb_function(input_string);
//     } else {
//         var prefix = input_string.substr(0, latex_start_index);
//         var latex_end_index = input_string.indexOf("</latex>");
//         var latex_length = latex_end_index - latex_start_index;
//         var suffix = input_string.substr(
//             latex_end_index + 8,
//             input_string.length - (latex_end_index + 8)
//         );
//         var latex = input_string.substr(
//             latex_start_index + 7,
//             latex_end_index - (latex_start_index + 7)
//         );
//         // console.log("latex_end_index", latex_end_index);
//         // console.log("latex_length", latex_length);
//         // console.log("prefix=" + prefix);
//         // console.log("suffix=" + suffix);
//         // console.log("latex=" + latex);
//         console.log("Start to convert latex", latex.replace(/\//gi, "\\"));
//         mjAPI.typeset({
//             math: latex.replace(/\//gi, "\\"),
//             format: "TeX", // or "inline-TeX", "MathML"
//             svg: true // or svg:true, or html:true
//         },
//         function(data) {
//             if (!data.errors) {
//                 console.log("Done convert latex", latex);
//                 replace_latex(suffix, function(output) {
//                     cb_function(prefix + data.svg + output);
//                 });
//             } else { console.log(data.errors); }
//         }
//         );
//     }
// }

// function parameters_to_string(parameter_list, max_list) {
//     // parameters in a list of positive integers
//     // max list is the max value of each parameter in a positive integer
//     // the sequence is important
//     var result=parameter_list[0];
//     for(var i=1;i<max_list.length;i++){
// result=result*max_list[i-1]+parameter_list[i];
//     }
//     return result.toString(36);
// }

// function string_backto_parameters(input_string,max_list){
//   var result=max_list;
//   var input=parseInt(input_string,36);

// }
// function try_js_py() {
//     var ps = require('python-shell');
//     var options = {
//         args: [
//             10, // number of simulations
//             2,
//             3,
//             4,
//             5,
//             60,
//             "a"
//         ]
//     }
//     ps.PythonShell.run('./js_interface.py', options, function(err, results) {
//         if (err)
//             console.log(err);
//         else {
//             console.log('finished');
//             console.log(results);
//             // console.log(results['problem_list'])
//         }
//     });
// }
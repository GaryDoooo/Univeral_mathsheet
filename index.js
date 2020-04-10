"use strict";

const socket = require("socket.io"), // socket for serving the chat service
    express = require("express"),
    path = require("path"),
    app = express(),
    server = require("http").Server(app),
    server_io = socket(server); // the io for chat server

/////// set the http listen and httpd working directory
app
    .set("view engine", "html")
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

    socket.on("gen", function(
        problem_num,
        question_type_list_string,
        cb_function
    ) {
        try {
            var ps = require("python-shell");
            var options = {
                args: [
                    problem_num,
                    question_type_list_string,
                    "new", // new means to generate new page key
                ],
            };
            ps.PythonShell.run("./js_interface.py", options, function(err, results) {
                if (err) {
                    console.log(err);
                    cb_function({
                        done: err
                    });
                } else {
                    console.log("finished");
                    console.log(results);
                    results=replace_latex_for_multiple__strings(results);
                    cb_function({
                        done: true,
                        problem_list: results[0],
                        answer_list: results[1],
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

    socket.on("answer", function(problem_num, page_key, cb_function) {
        try {
            var ps = require("python-shell");
            var options = {
                args: [
                    problem_num,
                    "a",
                    page_key, // if page key not 'new' means to get answers back
                ],
            };
            ps.PythonShell.run("./js_interface.py", options, function(err, results) {
                if (err) {
                    console.log(err);
                    cb_function({
                        done: err
                    });
                } else {
                    console.log("finished");
                    console.log(results);
                    cb_function({
                        done: true,
                        problem_list: results[0],
                        answer_list: results[1],
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

////////////////////////////////////////////////////////////////
// change latex in multiple strings
function replace_latex_for_multiple__strings(input_strings){
    var number_of_strings= input_strings.length;
    var number_of_done=Array(number_of_strings).fill(0); 
    var results=Array(number_of_strings).fill("");
    for (var i=0;i<number_of_strings;i++){
        replace_latex(input_strings[i],
            function(result){
                results[i]=result;
                number_of_done[i]=1;
            });
    }
    while(number_of_done.reduce((a, b) => a + b, 0)<number_of_strings){
        var i=1;
        i++; // use the while loop to wait all the results are ready 
    }
    return results;
} 
////////////////////////////////////////////////////////////////
// Using MathJax to convert TeX into svg 

var mjAPI = require("mathjax-node");
mjAPI.config({
    MathJax: {
    // traditional MathJax configuration
    },
});
mjAPI.start();

function replace_latex(input_string, cb_function) {
    var latex_start_index = input_string.indexOf("<latex>");
    console.log("latex_start_index", latex_start_index);
    if (latex_start_index == -1) {
        cb_function(input_string);
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
        console.log("latex_end_index", latex_end_index);
        console.log("latex_length", latex_length);
        console.log("prefix=" + prefix);
        console.log("suffix=" + suffix);
        console.log("latex=" + latex);
        mjAPI.typeset(
            {
                math: latex,
                format: "TeX", // or "inline-TeX", "MathML"
                svg: true, // or svg:true, or html:true
            },
            function (data) {
                if (!data.errors) {
                    replace_latex(suffix, function (output) {
                        cb_function(prefix + data.svg + output);
                    });
                }
            }
        );
    }
}

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
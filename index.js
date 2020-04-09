'use strict';

const socket = require('socket.io'), // socket for serving the chat service
    express = require("express"),
    path = require("path"),
    app = express(),
    server = require('http').Server(app),
    server_io = socket(server); // the io for chat server

var tex2svg = require( 'tex-equation-to-svg' );
var eqn = 'y = mx + b';

tex2svg( eqn, 

function clbk( error, svg ) {
	if ( error ) {
		throw error;
	}
	console.log( svg );}
);
/////// set the http listen and httpd working directory
app.set('view engine', 'html')
    .get('/', function(req, res) {
        res.sendFile(path.join(__dirname + '/public/'));
    })
    .use(express.static(path.join(__dirname, 'public')));

if (module === require.main) {
    const PORT = process.env.PORT || 8080;
    server.listen(PORT, () => {
        console.log(`App listening on port ${PORT}`);
        console.log('Press Ctrl+C to quit.');
    });
}

// try_js_py()

server_io.on('connection', function(socket) {
    console.log(`made socket connection ${socket.id}`, socket.id);

    socket.on('gen', function(
        problem_num, question_type_list_string,
        cb_function) {
        try {
            var ps = require('python-shell');
            var options = {
                args: [
                    problem_num, 
			question_type_list_string, "new" // new means to generate new page key
                ]
            }
            ps.PythonShell.run('./js_interface.py', options, function(err, results) {
                if (err) {
                    console.log(err);
                    cb_function({ 'done': err });
                } else {
                    console.log('finished');
                    console.log(results);
                    cb_function({
                        'done': true,
                        'problem_list': results[0],
                        'answer_list': results[1],
                        // 'page_key': results[2]
                    });
                    // console.log(results['problem_list'])
                }
            });
        } catch (err) {
            cb_function({ "done": err });
        }
    });

    socket.on('answer', function(problem_num, page_key, cb_function) {
        try {
            var ps = require('python-shell');
            var options = {
                args: [
                    problem_num,
                    "a", page_key // if page key not 'new' means to get answers back
                ]
            }
            ps.PythonShell.run('./js_interface.py', options, function(err, results) {
                if (err) {
                    console.log(err);
                    cb_function({ 'done': err });
                } else {
                    console.log('finished');
                    console.log(results);
                    cb_function({
                        'done': true,
                        'problem_list': results[0],
                        'answer_list': results[1],
                        // 'page_key': results[2]
                    });
                    // console.log(results['problem_list'])
                }
            });
        } catch (err) {
            cb_function({ 'done': err });
        }
    });
}); /// end of io connect

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

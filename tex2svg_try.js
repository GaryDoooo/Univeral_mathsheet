// var tex2svg = require("tex-equation-to-svg");

// tex2svg("y = mx + b", function clbk(error, svg) {
//   if (error) {
//     throw error;
//   }
//   console.log(svg);
// });

var mjAPI = require("mathjax-node");
mjAPI.config({
  MathJax: {
    // traditional MathJax configuration
  },
});
mjAPI.start();

// var yourMath = "1+1\times2";
// console.log(yourMath.raw);

// mjAPI.typeset(
//   {
//     math: yourMath.raw,
//     format: "TeX", // or "inline-TeX", "MathML"
//     svg: true, // or svg:true, or html:true
//   },
//   function (data) {
//     if (!data.errors) {
//       console.log(data.svg);
//     }
//   }
// );

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

var input_string0 = String.raw`<table BORDERCOLOR=white><tr><th colspan="5">ANSWER KEY:  22YK</th></tr><tr><td>[1] <latex>37\times8-67\times8=</latex></td><td>[2] <latex>22\times3-22\times13=</latex></td><td>[3] <latex>8\times28+8\times22=</latex></td>  </tr></table>`;
console.log(input_string0.indexOf("<latex>"), "\n"); //output 84
console.log(input_string0.substr(0, 84), "\n");
console.log(input_string0.indexOf("<latdddex>"), "\n");
console.log(
  input_string0.indexOf("</latex>"),
  input_string0.substr(84 + 7, 109 - (84 + 7)),
  "\n"
);
replace_latex(input_string0, function (output) {
  console.log(1, output);
});

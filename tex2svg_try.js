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

// var yourMath = "1+1";

// mjAPI.typeset(
//   {
//     math: yourMath,
//     format: "TeX", // or "inline-TeX", "MathML"
//     svg: true, // or svg:true, or html:true
//   },
//   function (data) {
//     if (!data.errors) {
//       console.log(data.svg);
//     }
//   }
// );

input_string =
  '<table BORDERCOLOR=white><tr><th colspan="5">ANSWER KEY:  22YK</th></tr><tr><td>[1] <latex>37\times8-67\times8=</latex></td><td>[2] <latex>22\times3-22\times13=</latex></td><td>[3] <latex>8\times28+8\times22=</latex></td>  </tr></table>';
console.log(input_string.indexOf("<latex>"));

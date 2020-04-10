var mjAPI = require("mathjax-node");
mjAPI.config({
  MathJax: {
    // traditional MathJax configuration
  },
});
mjAPI.start();

var yourMath = String.raw`1+1\times2`;
// console.log(yourMath);

mjAPI.typeset(
  {
    math: yourMath,
    format: "TeX", // or "inline-TeX", "MathML"
    svg: true, // or svg:true, or html:true
  },
  function (data) {
    if (!data.errors) {
      console.log(data.svg);
    }
  }
);

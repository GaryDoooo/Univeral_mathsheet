var mjAPI = require("mathjax-node");
mjAPI.config({
    MathJax: {
        // traditional MathJax configuration
    },
});
mjAPI.start();

var yourMath = String.raw `1+1\times 2`;
// console.log(yourMath);

mjAPI.typeset({
    math: yourMath,
    format: "TeX", // or "inline-TeX", "MathML"
    svg: true, // or svg:true, or html:true
},
function(data) {
    if (!data.errors) {
        console.log(data.svg);
    }
}
);

function fix_python_backslash_error(input_string) {
    var replace_table = [
        // [String.raw `\\div`, String.raw `\div`],
        // ["\\div", "\div"],
        // ["\\div", "\div"],
        ["/", "\\"]
    ];
    for (var i = 0; i < input_string.length; i++) {
        for (var j = 0; j < replace_table.length; j++) {
            console.log(input_string[i]);
            input_string[i].replace(replace_table[j][0], replace_table[j][1]);
            console.log(replace_table[j][0], replace_table[j][1]);
            console.log(input_string[i]);
        }
    }
    return input_string;
}

console.log(fix_python_backslash_error(
    ["4\\div 5", "3/div 4"]
));
console.log("3/div 5".replace("/", "\\"));

mjAPI.typeset({
    math: "1\\div 3",
    format: "TeX", // or "inline-TeX", "MathML"
    svg: true, // or svg:true, or html:true
},
function(data) {
    if (!data.errors) {
        console.log(data.svg);
    }
}
);
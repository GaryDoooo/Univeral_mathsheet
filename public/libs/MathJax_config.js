MathJax = {
    // tex: {
    //     inlineMath: [
    //         ["$$", "$$"],
    //         ["\\(", "\\)"],
    //         ["$", "$"]
    //         // ["<latex>", "</latex>"]
    //     ]
    // },
    svg: {
        scale: 1, // global scaling factor for all expressions
        minScale: .75, // smallest scaling factor to use
        mtextInheritFont: false, // true to make mtext elements use surrounding font
        merrorInheritFont: true, // true to make merror text use surrounding font
        mathmlSpacing: false, // true for MathML spacing rules, false for TeX rules
        skipAttributes: {}, // RFDa and other attributes NOT to copy to the output
        exFactor: .5, // default size of ex in em units
        displayAlign: "center", // default for indentalign when set to 'auto'
        displayIndent: "0", // default for indentshift when set to 'auto'
        fontCache: "local", // or 'global' or 'none'
        localID: null, // ID to use for local font cache (for single equation processing)
        internalSpeechTitles: true, // insert <title> tags with speech content
        titleID: 0 // initial id number to use for aria-labeledby titles
    }
};
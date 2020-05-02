localStorage.setItem("stage", "login");

var socket = io();
var abstrat_list_HTML_all_hidden = "";

window.addEventListener("load", function() {
    // added by gdu to update selection list
    var select_list = document.getElementById("ss_imp_list");
    var abstrat_list = document.getElementById("ss_live_region");
    socket.emit("GetListHTML", function(result) {
        select_list.innerHTML = result["selection_list"];
        abstrat_list.innerHTML = result["abstract_list"];
        abstrat_list_HTML_all_hidden = result["abstract_list"]; //.replace(/\//gi, "\\");
        console.log("load mathjax");

    });

    // Original selection list control code
    var ex1 = document.getElementById("ex1");
    var ex1ImportantListbox = new aria.Listbox(
        document.getElementById("ss_imp_list")
    );
    var ex1Toolbar = new aria.Toolbar(ex1.querySelector("[role=\"toolbar\"]"));
    var ex1UnimportantListbox = new aria.Listbox(
        document.getElementById("ss_unimp_list")
    );

    ex1ImportantListbox.setupMove(
        document.getElementById("ex1-delete"),
        ex1UnimportantListbox
    );
    ex1ImportantListbox.setHandleItemChange(function(event, items) {
        var updateText = "";
        if (updateText) {
            var ex1LiveRegion = document.getElementById("ss_live_region");
            ex1LiveRegion.innerText = updateText;
        }
    });
    ex1ImportantListbox.setHandleFocusChange(function(event, items) {
        // console.log("Focus change event", event, "    items", items);
        // console.log("event's id", event.id); // event is the li element focused newly
        var abstrat_list = document.getElementById("ss_live_region");
        abstrat_list.innerHTML = abstrat_list_HTML_all_hidden;
        var abstrat_to_show = document.getElementById(event.id + "_abs");
        abstrat_to_show.classList.remove("hidden");
        var abstrat_to_show = document.getElementById(event.id + "_abs_table");
        abstrat_to_show.classList.remove("hidden");
        MathJax.typeset();
    });
    ex1UnimportantListbox.setupMove(
        document.getElementById("ex1-add"),
        ex1ImportantListbox
    );
});

var problem_num_html = document.getElementById("problem_num"),
    num_of_col_html = document.getElementById("num_of_col"),
    generate = document.getElementById("generate"),
    prob_per_page_html = document.getElementById("prob_per_page"),
    problem_num_answer_html = document.getElementById("problem_num_answer"),
    col_num_answer_html = document.getElementById("col_num_answer"),
    page_key_html = document.getElementById("page_key"),
    select_list_html = document.getElementById("ss_unimp_list"),
    get_answer = document.getElementById("get_answer");

generate.addEventListener("click", function() {
    console.log("Key pressed generate");
    // console.log(select_list_html.innerHTML);
    var problem_num = get_number(problem_num_html.value, 100),
        num_of_col = get_number(num_of_col_html.value, 5),
        prob_per_page = get_number(prob_per_page_html.value, 100),
        page_count = 0,
        page_break_before = "<P style=\"page-break-before: always\">",
        problem_output = "",
        answer_output = "",
        total_pages = Math.ceil(problem_num / prob_per_page);

    // add selected list items into a string delim by ","
    if ((select_list_html.children.length > 0) && (problem_num <= 2000)) {
        var selected_list = select_list_html.children[0].id;
        for (var i = 1; i < select_list_html.children.length; i++) {
            selected_list =
                selected_list + "," + select_list_html.children[i].id;
        }
        console.log("Selection list sent:", selected_list);

        for (var i = 0; i < problem_num; i += prob_per_page) {
            socket.emit(
                "gen",
                Math.min(prob_per_page, problem_num - i),
                num_of_col,
                selected_list,
                function(result) {
                    if (page_count > 0) {
                        problem_output += page_break_before;
                        answer_output += page_break_before;
                    }
                    page_count++;
                    if (result["done"] == true) {
                        // go_next(result['problem_list'],result['answer_list']);
                        problem_output += result["problem_list"];
                        answer_output += result["answer_list"];
                        if (page_count >= total_pages) {
                            problem_output = replace_keys_to_shorter(
                                problem_output
                            );
                            answer_output = replace_keys_to_shorter(
                                answer_output
                            );
                            go_next(problem_output, answer_output);
                        }
                    } else {
                        console.log(result["done"]);
                    }
                }
            );
        }
    } else {
        alert("No seleted topics for the math sheet; or too many problems to generate.");
    }
});

get_answer.addEventListener("click", function() {
    var problem_num = get_number(problem_num_answer_html.value, 100),
        col_num = get_number(col_num_answer_html.value, 5);
    console.log("clicked get answer.");
    socket.emit(
        "answer",
        problem_num,
        col_num,
        replace_keys_to_longer(page_key_html.value),
        function(result) {
            if (result["done"] == true) {
                problem_output = replace_keys_to_shorter(
                    result["problem_list"]
                );
                answer_output = replace_keys_to_shorter(result["answer_list"]);
                go_next(answer_output, problem_output);
            } else {
                alert("Answer retrieving error.");
                console.log(result["done"]);
            }
        }
    );
});

function replace_keys_to_longer(input_string) {
    result = input_string.replace("#", "5LSA1EU-8IKG0-");
    result = result.replace("@", "5LS8BJ2-8IKG0-");
    result = result.replace("$", "4BP42J69Y-TKHGUA-");
    return result;
}

function replace_keys_to_shorter(input_string) {
    result = input_string.replace(/4BP42J69Y-TKHGUA-/gi, "$");
    result = result.replace(/5LS8BJ2-8IKG0-/gi, "@");
    result = result.replace(/5LSA1EU-8IKG0-/gi, "#");
    return result;
}

function go_next(problem_list, answer_list) {
    localStorage.setItem("problem_list", problem_list);
    localStorage.setItem("answer_list", answer_list);
    window.location.href = "chat.html";
}

function get_number(text, system_default = 10, radix = 10) {
    result = parseInt(text, radix);
    if (result == NaN) {
        result = system_default;
    }
    return result;
}
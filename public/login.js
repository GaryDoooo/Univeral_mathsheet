localStorage.setItem("stage", "login");

var socket = io();
var problem_num_html = document.getElementById("problem_num"),
    num_of_col_html = document.getElementById("num_of_col"),
    generate = document.getElementById("generate"),
    prob_per_page_html = document.getElementById("prob_per_page"),
    problem_num_answer_html = document.getElementById("problem_num_answer"),
    col_num_answer_html = document.getElementById("col_num_answer"),
    page_key_html = document.getElementById("page_key"),
    get_answer = document.getElementById("get_answer");

generate.addEventListener("click", function() {
    var problem_num = get_number(problem_num_html.value, 100),
        num_of_col = get_number(num_of_col_html.value, 5),
        prob_per_page = get_number(prob_per_page_html.value, 100),
        page_count = 0,
        page_break_before = "<P style=\"page-break-before: always\">",
        problem_output = "",
        answer_output = "",
        total_pages = Math.ceil(problem_num / prob_per_page);
    for (var i = 0; i < problem_num; i += prob_per_page) {
        socket.emit(
            "gen",
            Math.min(prob_per_page, problem_num - i), num_of_col,
            "chengfahebing",
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
                        problem_output = replace_keys_to_shorter(problem_output);
                        answer_output = replace_keys_to_shorter(answer_output);
                        go_next(problem_output, answer_output);
                    }
                } else {
                    console.log(result["done"]);
                }
            }
        );
    }
});

get_answer.addEventListener("click", function() {
    var problem_num = get_number(problem_num_answer_html.value, 100),
        col_num = get_number(col_num_answer_html.value, 5);
    console.log("clicked get answer.");
    socket.emit(
        "answer",
        problem_num, col_num,
        replace_keys_to_longer(page_key_html.value),
        function(result) {
            if (result["done"] == true) {
                problem_output = replace_keys_to_shorter(result["problem_list"]);
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
// Make connection socket

// const key = client_random_key_gen(); // get the unique random key for this session
var stage = localStorage.getItem("stage");
if (stage === "login") {
    localStorage.setItem("stage", "chat");
} else {
    window.location.href = "index.html";
} /////check if it's reload from itself, if so kick back to login screen.

var problem_list = localStorage.getItem("problem_list");
var answer_list = localStorage.getItem("answer_list");
var current_display = 0;
console.log("Got result.\n", problem_list, answer_list);

var output = document.getElementById('output'),
    swap = document.getElementById('swap');

output.innerHTML = problem_list;

// Emit events
// Detect the click event on send key
swap.addEventListener('click', function() {
    current_display += 1;
    if (current_display % 2 == 0) {
        output.innerHTML = problem_list;
    } else {
        output.innerHTML = answer_list;
    }
});
// Detect the ENTER key pressed inside the message input box
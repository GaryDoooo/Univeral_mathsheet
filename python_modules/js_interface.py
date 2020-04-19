import sys
from math_gen import dispatch, html_output

problem_num = int(sys.argv[1])
#  first_num_min = int(sys.argv[2])
#  first_num_max = int(sys.argv[3])
#  second_num_min = int(sys.argv[4])
#  second_num_max = int(sys.argv[5])
#  result_max = int(sys.argv[6])
question_type_list_string = sys.argv[3]
page_key = sys.argv[4]
num_of_col = sys.argv[2]

problem_list, answer_list, page_key = dispatch(
    question_type_list_string, problem_num,
    page_key
)
problem_output, answer_output = html_output(
    problem_list, answer_list, page_key, num_of_col)
# result={
# 	"problem_list":problem_output,
# 	"answer_list":answer_output
# }

print(repr(problem_output))
# repr(STR) prints the raw string, ingnore \t \n formatting things
print(repr(answer_output))
# print(page_key)
sys.stdout.flush()

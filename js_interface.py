import sys
from math_gen import dispatch, html_output

problem_num = int(sys.argv[1])
first_num_min = int(sys.argv[2])
first_num_max = int(sys.argv[3])
second_num_min = int(sys.argv[4])
second_num_max = int(sys.argv[5])
result_max = int(sys.argv[6])
operator = sys.argv[7]
page_key = sys.argv[8]

problem_list, answer_list, page_key = dispatch(first_num_max,
                                               second_num_max,
                                               result_max,
                                               first_num_min,
                                               second_num_min,
                                               operator,
                                               problem_num,
                                               page_key
                                               )
problem_output, answer_output = html_output(
    problem_list, answer_list, page_key)

# result={
# 	"problem_list":problem_output,
# 	"answer_list":answer_output
# }

print(problem_output)
print(answer_output)
# print(page_key)
sys.stdout.flush()

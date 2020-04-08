from chengfahebing import function_list as chengfahebing_function_list
from chengfahebing import *

function_list = []
function_list.extend(chengfahebing_function_list)
#  print(function_list)
selected_question_types = ['chengfahebing']
function_list_to_use = []
for function in function_list:
    selected = False
    for question_type in selected_question_types:
        if question_type in function:
            selected = True
    if selected:
        function_list_to_use.append(function)
#  print(function_list_to_use)
#  print(equation_chengfahebing_plus_10())

html_header="<html><head><title>Math Generator</title></head><body>"
table_header="<table style='width:100%'>"

#  <table style="width:100%">
  #  <tr>
    #  <th>Firstname</th>
    #  <th>Lastname</th>
    #  <th>Age</th>
  #  </tr>
  #  <tr>
    #  <td>Jill</td>
    #  <td>Smith</td>
    #  <td>50</td>
  #  </tr>
  #  <tr>
    #  <td>Eve</td>
    #  <td>Jackson</td>
    #  <td>94</td>
  #  </tr>
#  </table>

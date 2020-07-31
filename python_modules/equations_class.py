from importlib import import_module
import random
from page_key import page_key_compress
from page_key import page_key_decompress

# New elements to the list shoud be added always from the end of the list
# otherwise, the problem key will not work correctly.
global_module_list = [
    "chengfahebing",
    "chufahebing_w_frac",
    "chufahebing",
    "chengfahebing_w_frac",
    "fraction_basic",
    "exponent_compare",
    "two_symbol_expand1",
    "two_symbol_expand2",
    "exponent_consolidate",
    "exponent_consolidate2",
    "linear_eq_1unknown"
]
# the first max is the 2 power of number of diffuser modules, 2147483647
# is 32 bit integer, so far the program is good for 32 different modules.
# The second max is for random seed
# in the future can add catagories, which is the 3rd variable, while each
# catagory allows max 32 modules
max_list = [2147483647, 65535]

#  class equation_generator:


class equation:

    def __init__(self, module_list=global_module_list):
        self.module_list = module_list
        self.module = {}
        for _ in self.module_list:
            # In Python to import a py module under a directory, use
            # dir_name.module_name instead of dir_name/module_name
            _m = import_module("Q_Gen_modules." + _)
            self.module.update({_: _m})
        self.add_absract_samples()

    def li_html(self):
        #  return [_.abstract for _ in self.module]
        #  <li id="ss_opt1" role="option">
        #  Proximity of public K-12 schools
        #  </li>
        selection_html = ""
        abstract_html = ""
        index = 0
        for module_name in self.module_list:
            index += 1
            selection_html += '<li id="%s" role="option">%s</li>' % (
                module_name, "%d) " % index + self.module[module_name].list_name)
            abstract_html += ('<li id="' + module_name + "_abs" +
                              '" role="option" class="hidden">' +
                              self.module[module_name].abstract +
                              "</li>" +
                              self.abstract_sample_table[module_name]
                              )
        return selection_html, abstract_html

    def add_absract_samples(self):
        # table_head = '<table width="100%"><tr>'
        table_end = "  </tr></table>"
        self.abstract_sample_table = {}
        for module_name in self.module_list:
            table_HTML_string = (
                '<table width="100%" id="' +
                module_name +
                '_abs_table" class="hidden" role="table"><tr>' +
                "<td>" +
                "<latex>" +
                self.generate_a_question(module_name)[0] +
                "</latex></td><td>" +
                "<latex>" +
                self.generate_a_question(module_name)[0] +
                "</latex></td></tr><tr><td>" +
                "<latex>" +
                self.generate_a_question(module_name)[0] +
                "</latex></td><td>" +
                "<latex>" +
                self.generate_a_question(module_name)[0] +
                "</latex></td>" + table_end)
            self.abstract_sample_table.update({module_name:
                                               table_HTML_string})
        # below for debugging
        result = ""
        for module_name in self.module_list:
            result += module_name + " Abstract:\n" + \
                self.abstract_sample_table[module_name] + "\n"
        return result  # the result here is just for debugging

    def generate_a_question(self, module_name):
        # a module from the equation class
        SubModule = self.module[module_name]
        # a string of name of the function
        function_to_run = random.choice(SubModule.function_list)
        return call(SubModule, function_to_run)

    def encode_key(self, question_type_list, randseed):
        binary_code = ""
        for module_name in self.module_list:
            if module_name in question_type_list:
                binary_code = "1" + binary_code
            else:
                binary_code = "0" + binary_code
        decimal_code = int(binary_code, 2)
        return page_key_compress([decimal_code, randseed], max_list)

    def decode_key(self, input_key):
        [decimal_code, randseed] = page_key_decompress(input_key, max_list)
        # output of bin() is 0b000010101 as a string
        binary_code = "0" * 32 + bin(decimal_code)[2:]
        result_list = []
        for i in range(len(self.module_list)):
            if binary_code[-1 - i] == "1":
                result_list.append(self.module_list[i])
        return result_list, randseed

    def sort_question_list(self, question_list):
        result_list = []
        for module_name in self.module_list:
            if module_name in question_list:
                result_list.append(module_name)
        return result_list

    def get_page_note(self, question_list):
        result = ""
        for module_name in question_list:
            try:
                result += self.module[module_name].note + " "
            except BaseException:
                pass
        return result


def call(module, function_name_suffix, var_list=None):
    # this is an importance methode: to call a function inside a module by its
    # name in a string
    function_to_run = getattr(module, "equation_" +
                              function_name_suffix.replace("equation_", ""))
    if var_list is None:
        return function_to_run()
    else:
        return function_to_run(var_list)


if __name__ == "__main__":
    a = equation()
    # print(a.add_absract_samples())
    #  print(a.li_html())
    print(a.encode_key(["chengfahebing", "chufahebing_w_frac"], 44))
    print(a.decode_key("13ypim"))
    print(a.get_page_note(["chengfahebing", "exponent_compare"]))

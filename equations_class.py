from importlib import import_module
import random

# New elements to the list shoud be added always from the end of the list
# otherwise, the problem key will not work correctly.
global_module_list = [
    "chengfahebing", "chufahebing_w_frac", "chufahebing", "chengfahebing_w_frac"]


#  class equation_generator:
class equation:

    def __init__(self, module_list=global_module_list):
        self.module_list = module_list
        self.module = {}
        for _ in self.module_list:
            _m = import_module(_)
            self.module.update({_: _m})
        self.add_absract_samples()

    def li_html(self):
        #  return [_.abstract for _ in self.module]
        #  <li id="ss_opt1" role="option">
        #  Proximity of public K-12 schools
        #  </li>
        selection_html = ""
        abstract_html = ""
        for module_name in self.module_list:
            selection_html += '<li id="%s" role="option">%s</li>' % (
                module_name, self.module[module_name].list_name)
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
            table_HTML_string = ('<table width="100%" id="' + module_name + '_abs_table" class="hidden" role="table"><tr>' +
                                 "<td>" +
                                 "<latex>" + self.generate_a_question(module_name)[0] + "</latex></td><td>" +
                                 "<latex>" + self.generate_a_question(module_name)[0] + "</latex></td></tr><tr><td>" +
                                 "<latex>" + self.generate_a_question(module_name)[0] + "</latex></td><td>" +
                                 "<latex>" +
                                 self.generate_a_question(module_name)[0] + "</latex></td>")
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


def call(module, function_name_suffix, var_list=None):
    # this is an importance methode: to call a function inside a module by its
    # name in a string
    function_to_run = getattr(module, "equation_" + function_name_suffix)
    if var_list is None:
        return function_to_run()
    else:
        return function_to_run(var_list)


if __name__ == "__main__":
    a = equation()
    # print(a.add_absract_samples())
    print(a.li_html())

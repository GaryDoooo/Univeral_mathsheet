from importlib import import_module

global_module_list = [
    "chengfahebing", "chufahebing_w_frac", "chufahebing", "chufahebing_w_frac"]


#  class equation_generator:
class equation:
    def __init__(self, module_list=global_module_list):
        self.module_list = module_list
        self.module = {}
        for _ in self.module_list:
            _m = import_module(_)
            self.module.update({_: _m})

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
            abstract_html += '<li id="%s" role="option">%s</li>' % (
                module_name + "_abs", self.module[module_name].abstract)
        return selection_html, abstract_html


if __name__ == "__main__":
    a = equation()
    print(a.li_html())

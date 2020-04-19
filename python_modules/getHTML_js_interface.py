import sys
from equations_class import equation

a = equation()
selection_html, abstract_html = a.li_html()

print(selection_html)
print(abstract_html)

sys.stdout.flush()

# ctrl D like in sublime Text
from IPython.display import display,Javascript
jsfile = urlopen('https://raw.githubusercontent.com/vincentAGNES/Jupyter-notebook/master/jupyter_js.js')
jscontent = jsfile.read().decode('utf-8')
jsfile.close()
Javascript(jscontent)
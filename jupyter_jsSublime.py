# ctrl D like in sublime Text
from IPython.display import Javascript
from urllib.request import urlopen
jsfile = urlopen('https://raw.githubusercontent.com/vincentAGNES/Jupyter-notebook/master/jupyter_jsSublime.js')
jscontent = jsfile.read().decode('utf-8')
jsfile.close()
Javascript(jscontent)
del jsfile

# DON'T FORGET TO REMOVE ME WHEN DEV IS DONE :)

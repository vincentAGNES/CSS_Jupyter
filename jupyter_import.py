# Classique 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

# Styling
from IPython.core.display import HTML
from urllib.request import urlopen

# ctrl D like in sublime Text
from IPython.display import display,Javascript
jsfile = urlopen('https://raw.githubusercontent.com/vincentAGNES/Jupyter-notebook/master/jupyter_js.js')
jscontent = jsfile.read().decode('utf-8')
jsfile.close()
Javascript(jscontent)

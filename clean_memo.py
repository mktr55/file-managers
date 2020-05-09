# %%
import os
#print(os.getcwd())
current_dir = os.path.dirname(os.path.abspath("__file__"))
print("current directory is {}".format(current_dir))
#os.chdir(current_dir)
#windows用
#os.chdir(r"C:\Users/"username"/Google ドライブ/learning/")
# %%

import glob
import subprocess
subprocess.call(["pip","install","pylint"])
subprocess.call(["pip","install","pysrt"])
import pysrt

subprocess.call(["pip","install","googletrans"])
#from googletrans import Translator

subprocess.call(["pip","install","pandas_profiling"])
subprocess.call(["pip","install","cufflinks"])

import time
import datetime


# %%

# import pandas as pd
# import pandas_profiling as pdp
# import seaborn as sns
#
# import cufflinks as cf
# # デフォでPlotlyのオンラインモードとなっているのでオフラインモードへと変更
# # 恒久的にデフォルトをオフラインモードとする方法は下に記述
# cf.go_offline()
#
# import plotly.plotly as py
# import plotly.offline as offline
# import plotly.graph_objs as go
# offline.init_notebook_mode()
#
# #Plotly初期化
# def configure_plotly_browser_state():
#   import IPython
#   display(IPython.core.display.HTML('''
#         <script src="/static/components/requirejs/require.js"></script>
#         <script>
#           requirejs.config({
#             paths: {
#               base: '/static/base',
#               plotly: 'https://cdn.plot.ly/plotly-latest.min.js?noext',
#             },
#           });
#         </script>
#         '''))

# %%
files = glob.glob("{}".format(current_dir)+"/*", recursive=False)

# %%

# %%
lists = []
for i in files:
  print(i[36:40])
  if i[36:40] =="2020":
    print(i)
    lists.append(i)
# %%

now = datetime.date.today()
print(now)
# %%
for i in lists:
  print(os.path.getctime(i))
  print(datetime.date.fromtimestamp(int(os.path.getctime(i))))

  ctime = datetime.date.fromtimestamp(int(os.path.getctime(i)))
  if (now - ctime).days > 7:
    print ("over 7days")
    subprocess.call(["mv",i,"{}".format(current_dir)+"/past_memox/"])

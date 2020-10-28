

from pandas_datareader import data
from yahooquery import Ticker
import matplotlib.pyplot as plt
import pandas as pd
from pandas_datareader import data as web
import plotly.graph_objects as go
import plotly
import os

if not os.path.exists("images"):
    os.mkdir("images")

ativo="PETR4.SA" 
start_date = '2020-10-19'
end_date = '2020-10-23'
df = web.DataReader(ativo, 'yahoo', start_date,end_date)

#df1= (df["Close"].to_string(header=False))
print("Consultando dados do "+ativo + " período inicio: "+ start_date + " Fim:" + end_date) 
trace1 = {
    'x': df.index,
    'open': df.Open,
    'close': df.Close,
    'high': df.High,
    'low': df.Low,
    'type': 'candlestick',
    'name': ativo,
    'showlegend': True
}
data= [trace1]
layout = go.Layout()

fig = go.Figure(data=data, layout=layout)
#fig.show()
plotly.offline.plot(fig, filename="C:/temp/images/"+ativo+".html", auto_open=False)



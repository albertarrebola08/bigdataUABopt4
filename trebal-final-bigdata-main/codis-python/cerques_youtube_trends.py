from pytrends.request import TrendReq
import plotly.express as px
import pandas as pd

pytrends = TrendReq(hl='es', tz=360)

kw_list = ["ahorrar"]
pytrends.build_payload(kw_list, cat=0, timeframe='2005-01-01 2024-01-01', geo='ES', gprop='youtube')

data = pytrends.interest_over_time()
data = data.reset_index()

data.to_csv("ahorrar.csv", index=False)

fig = px.line(data, x="date", y=kw_list, title='Interés de Búsqueda en YouTube a lo largo del Tiempo')
fig.show()

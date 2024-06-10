import requests
from bs4 import BeautifulSoup
import pandas as pd


#url IPC
url = 'https://www.idescat.cat/indicadors/?id=conj&n=10261&tema=PREUS&col=1'

#url Salaris
#url = 'https://www.idescat.cat/indicadors/?id=anuals&n=10400&tema=TREBA&col=3'



response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


table = soup.find('table')
df = pd.read_html(str(table))[0]

df.to_csv('catalunya_ipc.csv', index=False)

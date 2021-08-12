import requests as rt
import json
import pandas as pd

palavra = rt.get('http://dicionario-aberto.net/search-json/oi')
print(palavra)
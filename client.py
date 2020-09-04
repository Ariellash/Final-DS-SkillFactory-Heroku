import requests
import pandas as pd
import json
import ast

df = pd.read_json('test_example.json',orient='records')


if __name__=='__main__':
    r = requests.post('https://obscure-retreat-21347.herokuapp.com/predict', json=df.to_json(orient='records'))

    print(r.status_code)

    if r.status_code == 200:

        print(r.json())
    else:
        print(r.text)
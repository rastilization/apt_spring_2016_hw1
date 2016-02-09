from bottle import route, run, template
import requests
from bs4 import BeautifulSoup
import os 
import json

@route('/')
def index():
    return {"usd": 378, "eur": 415, "rub": 4.82}


URL = "http://public.mig.kz/"

@route('/forks')
def forks():
    resp = requests.get(URL)
    bs4 = BeautifulSoup(resp.content, "html.parser")	
    res = {}
    for tag in bs4.find_all('td'):
       	if tag.has_attr('class') and 'currency' in tag.attrs['class']:
        	res[tag.string] = tag.parent.find('td').string
    return json.dumps(res)

run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

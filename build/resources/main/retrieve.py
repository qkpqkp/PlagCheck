import requests, json
import re
from bs4 import BeautifulSoup

key = "AIzaSyB-UHIT2lz1Hw-XyeFAQ7dJW67mNWCDnKg"
cx = "007835117730733246990:1ek1-aykdo4"
query = "np.genfromtxt(Fvector, dtype=float, delimiter=',', names=True)"
search_url = "https://www.googleapis.com/customsearch/v1?key="+ key + "&cx=" + cx + "&q=" + query
content = requests.get(search_url)
json = json.loads(content.content)
for item in json["items"]:
    result_url=item["link"]
    #result_url = json["items"][0]["link"]
    result_url = "https://stackoverflow.com/questions/67176660/how-to-compare-2-excel-columns-using-dataframe-then-output-it-to-another-excel-f"
    if result_url.startswith("https://stackoverflow.com/"):
        r = requests.get(result_url)
        soup = BeautifulSoup(r.content, 'html5lib')
        pres = soup.find_all('pre')
        results = []
        for pre in pres:
            codes = pre.find_all('code')
            for code in codes:
                results.append(code.text)
        print(results[5])
    elif result_url.startswith("https://github.com/"):
        r = requests.get(result_url)
        soup = BeautifulSoup(r.content, 'html5lib')
        tbody = soup.find_all('tbody')
        results = []
        for code in tbody:
            results.append(code.text)
        print(results[0])
    break


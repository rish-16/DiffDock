import requests
from pprint import pprint
import urllib.request
import re, json
import pandas as pd
from bs4 import BeautifulSoup # pip install beautifulsoup4

FILE = "avail_gpcrmd_data.csv"
df = pd.read_csv(FILE)
gpcrmd_ids = df['GPCRmd_ID'].values.tolist()

print (gpcrmd_ids)

url_prefix = "https://submission.gpcrmd.org/dynadb/dynamics/id/"
dwld_prefix = "https://submission.gpcrmd.org/"

for i, idx in enumerate(gpcrmd_ids):
    try:
        if i % 50 == 0:
            print (f"Currently at sample {i}")

        URL = url_prefix + str(idx)
        html_page = urllib.request.urlopen(URL)
        soup = BeautifulSoup(html_page, 'html.parser')

        container = soup.select("div#hideall")[0]
        link_tags = container.find_all("a", href=True)
        dwld_urls = list(map(lambda x : x['href'], link_tags))

        URL_STORE[str(idx)] = []
        for url in dwld_urls:
            if url.endswith(".xtc") or url.endswith(".pdb"):
                URL_STORE[str(idx)].append(dwld_prefix + url)
    
    except Exception as e:
        print (f"Failed to fetch URLS for {str(idx)}")
        print (e)

pprint (URL_STORE)
with open('gpcrmd_ligand_link_store.json', "w") as f:
    json.dump(URL_STORE, f, indent=4)

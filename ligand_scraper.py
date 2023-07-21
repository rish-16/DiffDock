import requests
from pprint import pprint
import urllib.request
import re, json
import pandas as pd
from bs4 import BeautifulSoup # pip install beautifulsoup4

FILE = "avail_gpcrmd_data.csv"
df = pd.read_csv(FILE)
holo_idx = df['ConformationalType'] == "Holo"
gpcrmd_ids = df[holo_idx]['GPCRmd_ID'].values.tolist()
gpcrmd_conftypes = df['ConformationalType'].values.tolist()
gpcrmd_pdb_ids = df['PDB_ID'].values.tolist()

# print (gpcrmd_ids)
URL_STORE = {}
url_prefix = "https://submission.gpcrmd.org/dynadb/dynamics/id/"
dwld_prefix = "https://submission.gpcrmd.org/"

for i, idx in enumerate(gpcrmd_ids):
    try:
        # if i % 50 == 0:
            # print (f"Currently at sample {i}")

        URL = url_prefix + str(idx)
        html_page = urllib.request.urlopen(URL)
        soup = BeautifulSoup(html_page, 'html.parser')

        container = soup.select("div#bottoninfoleft")[0]
        # print (container)
        link_tags = container.select("a.btn.btn-primary", href=True)
        dwld_urls = list(map(lambda x : x['href'], link_tags))
        dwld_url = dwld_urls[0]
        fp = dwld_prefix + dwld_url

        mol_page = urllib.request.urlopen(fp)
        mol_soup = BeautifulSoup(mol_page, 'html.parser')

        container = mol_soup.select("div.container")[0]
        smiles_cont = container.select("div.panel-body")[0].text
        smiles_string = smiles_cont.split("<br>")[0].split(" ")[1]

        print (idx, dwld_url, smiles_cont.split("<br>")[0].split(" ")[1])
        URL_STORE[str(idx)] = {
            "string": smiles_string,
            "conftype": gpcrmd_conftypes[i],
            "PDB_ID": gpcrmd_pdb_ids[i],
            "GPCRmd_ID": str(idx)
        }
        
    except Exception as e:
        print (f"Failed to fetch URLS for {str(idx)}")
        print (e)

pprint (URL_STORE)
with open('gpcrmd_ligand_link_store.json', "w") as f:
    json.dump(URL_STORE, f, indent=4)

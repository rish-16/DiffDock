import os
from pprint import pprint
import pandas as pd

pdbbind_path = "PDBBind/PDBBind_processed/"
pdbbind_structures = []

gpcrmd_path = "GPCRmd/"
gpcrmd_structures = []

for item in os.listdir(pdbbind_path):
    pdbbind_structures.append(item.strip("/").lower().strip())

df = pd.read_csv("avail_gpcrmd_data.csv")
pdb_ids = df['PDB_ID'].values.tolist()
pdb_ids = [rec.lower().strip() for rec in pdb_ids]

pdbbind_structures = set(pdbbind_structures)
pdb_ids = set(pdb_ids)

common1 = list(pdbbind_structures.intersection(pdb_ids))
print (common1)
print (len(common1))

common2 = list(pdb_ids.intersection(pdbbind_structures))
print (common2)
print (len(common2))

test = ["3nya", "3ny8", "4ldo", "5d6l"]

for i in test:
    print (i)
    print (i in set(common1), i in set(common2))
    
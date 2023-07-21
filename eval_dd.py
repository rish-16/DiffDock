import MDAnalysis as mda
from pprint import pprint
import pandas as pd
import os, json

avail_struct_record = pd.read_csv("avail_gpcrmd_data.csv")
PDB_IDS = avail_struct_record['PDB_ID'].values.tolist()

"""
{
    PDBID: [
        [apo_path, holo_path, apo_ID, holo_ID],
        [apo_path, None, apo_ID, None],
        [None, holo_path, None, holo_ID],
    ],
}
"""

records = {}
for pdb in PDB_IDS:
    rec_idx = avail_struct_record['PDB_ID'] == pdb
    rec = avail_struct_record[rec_idx]
    ids = rec['GPCRmd_ID'].values.tolist()
    ids.sort()
    types = rec['ConformationalType'].values.tolist()

    assert len(types) == len(ids)

    apos = [ids[i] for i in range(len(ids)) if types[i] == "Apo"]
    holos = [ids[i] for i in range(len(ids)) if types[i] == "Holo"]

    records[pdb] = {
        'apo': apos,
        'holo': holos
    }

# print (records)
avail_recs = {item : val for item, val in records.items() if len(val['apo']) >= 1 and len(val['holo']) >= 1} # find pairs where both an apo and holo structure exist

with open("gpcrmd_ligand_link_store.json", "r") as f:
    ligand_recs = json.load(f)

# create inference CSV
print ("complex_name,protein_path,ligand_description")
for i, (pdb, ids) in enumerate(avail_recs.items()):
    """
    PDBID
        apo.pdb
        holo.pdb
        ligand.sdf
    """

    apos, holos = ids['apo'], ids['holo']

    k = min(len(apos), len(holos))

    for j in range(k):
        first_apo_id = apos[j]
        first_holo_id = holos[j]
    
        if str(first_holo_id) in ligand_recs:
            smiles_string = ligand_recs[str(first_holo_id)]['string']
            if smiles_string != "":
                pdb_id = ligand_recs[str(first_holo_id)]['PDB_ID']
                path = f"GPCRmd/gpcrmd_ID_{str(first_apo_id)}/"
                fp = os.listdir(path)[0]
                path = path + fp
                print (f"{pdb_id}_{str(i+1)},{path},{smiles_string}")
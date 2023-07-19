"""
for all shared PDBs, get their RMSD similarity between 
the 5 test samples
"""

import os
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt
import MDAnalysis as mda
from MDAnalysis.analysis import rms

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

test_pdb_ids = ["3nya", "3ny8", "4ldo", "5d6l"]
test_gpcrmd_ids = [100, 88, 116, 962]

pairs = [
    ["3NY8", "gpcr_tests/3NY8_5089/10853_dyn_88_apo.pdb", "gpcr_tests/3NY8_5089/11186_dyn_123_holo.pdb", "gpcr_tests/3NY8_5089/11178_mol_5089.sdf"],
    ["3NYA", "gpcr_tests/3NYA_5091/10957_dyn_100_apo.pdb", "gpcr_tests/3NYA_5091/11198_dyn_124_holo.pdb", "gpcr_tests/3NYA_5091/11190_mol_5091.sdf"],
    ["5D6L", "gpcr_tests/5D6L_5216/18125_dyn_962_apo.pdb", "gpcr_tests/5D6L_5216/18127_dyn_963_holo.pdb", "gpcr_tests/5D6L_5216/13458_mol_5216.sdf"],
    ["4LDO", "gpcr_tests/4LDO_5080/11109_dyn_116_apo.pdb", "gpcr_tests/4LDO_5080/11159_dyn_117_holo.pdb", "gpcr_tests/4LDO_5080/11122_mol_5080.sdf"]
]    

for pair in pairs:
    pdb_id, apo_fp, holo_fp, ligand_fp = pair

    apo_uni = mda.Universe(apo_fp, format="PDB")
    holo_uni = mda.Universe(holo_fp, format="PDB")

    apo_protein = apo_uni.select_atoms("protein")
    holo_protein = holo_uni.select_atoms("protein")
    print (apo_protein.positions.shape, holo_protein.positions.shape)

    r = rms.rmsd(apo_protein.positions, holo_protein.positions)
    print (f"Apo-Holo RMSD for {pdb_id}: {r:.5f}")
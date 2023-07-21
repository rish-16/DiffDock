import json, re, os, pycurl, subprocess

STORE_PATH = "gpcrmd_dwld_store.json"
# SAVE_PATH = "gpcrmd_mass_dwld.sh"

with open(STORE_PATH, "r") as f:
    store = json.load(f)

for gpcrmd_ID, links in store.items():
    new_path = f"gpcrmd_ID_{str(gpcrmd_ID)}"
    
    print (f"mkdir {new_path}")
    print (f"cd {new_path}")
    for link in links:
        print (f"curl -O {link}")
    print ("cd ..")
    print ("")
    print ("")

"""
"908": [
    "https://submission.gpcrmd.org/dynadb/files/Dynamics/16502_trj_908.xtc",
    "https://submission.gpcrmd.org/dynadb/files/Dynamics/16503_trj_908.xtc",
    "https://submission.gpcrmd.org/dynadb/files/Dynamics/16504_trj_908.xtc",
    "https://submission.gpcrmd.org/dynadb/files/Dynamics/18021_dyn_908.pdb"
],
"909": [
    "https://submission.gpcrmd.org/dynadb/files/Dynamics/16509_trj_909.xtc",
    "https://submission.gpcrmd.org/dynadb/files/Dynamics/16510_trj_909.xtc",
    "https://submission.gpcrmd.org/dynadb/files/Dynamics/16511_trj_909.xtc",
    "https://submission.gpcrmd.org/dynadb/files/Dynamics/18023_dyn_909.pdb"
],
"87": [
    "https://submission.gpcrmd.org/dynadb/files/Dynamics/10840_trj_87.xtc",
    "https://submission.gpcrmd.org/dynadb/files/Dynamics/10841_trj_87.xtc",
    "https://submission.gpcrmd.org/dynadb/files/Dynamics/10842_trj_87.xtc",
    "https://submission.gpcrmd.org/dynadb/files/Dynamics/10844_dyn_87.pdb"
],
"""
import json, re, os, pycurl, subprocess

STORE_PATH = "gpcrmd_dwld_store.json"

print ("Saving in:", os.getcwd())

with open(STORE_PATH, "r") as f:
    store = json.load(f)

for gpcrmd_ID, links in store.items():
    new_path = f"gpcrmd_ID_{str(gpcrmd_ID)}"
    os.mkdir(new_path)
    
    print (f"Saving at {new_path}/")
    try:
        for link in links:
            cmd1 = f"cd {new_path} && curl -O {link} && cd .."
            subprocess.call(cmd1, shell=True)
    except:
        print (f"Unable to download files for {gpcrmd_ID}")

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
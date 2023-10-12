############################################
# Inventory.py
# Inventory system
############################################

inventory = {
    "Mission1Job1Choice1": False,
    "Mission1Job1Choice2": False,
    "Mission1Job1Choice3": False,
    "Mission1Job2Choice1": False,
    "Mission1Job2Choice2": False,
    "Mission1Job2Choice3": False,
    "Mission1Complete": False,
    "Mission2Job1Choice1": False,
    "Mission2Job1Choice2": False,
    "Mission2Job1Choice3": False,
    "Mission2Job2Choice1": False,
    "Mission2Job2Choice2": False,
    "Mission2Job2Choice3": False,
    "Mission2Complete": False,
    "Mission3Job1Choice1": False,
    "Mission3Job1Choice2": False,
    "Mission3Job1Choice3": False,
    "Mission3Job2Choice1": False,
    "Mission3Job2Choice2": False,
    "Mission3Job2Choice3": False,
    "Mission3Complete": False
}


# Funcție pentru setarea statusului unei sub-misiuni
def set_sub_mission_status(mission_id, job_id, choice_id, status=True):
    key = f"Mission{mission_id}Job{job_id}Choice{choice_id}"
    inventory[key] = status


# Funcție pentru verificarea statusului unei sub-misiuni
def check_sub_mission_status(mission_id, job_id, choice_id):
    key = f"Mission{mission_id}Job{job_id}Choice{choice_id}"
    return inventory.get(key, False)


# Functie ce verifica daca vreuna o submisiune are completata oricare din optiuni
# Cand se apeleaza funcția cu check_mission_status_for_job(3, 2), în interiorul funcției, pentru fiecare choice_id
# de la 1 la 3, se va genera un key de forma Mission3Job2Choice1, Mission3Job2Choice2, și Mission3Job2Choice3
# pentru a verifica în inventory.
def check_mission_status_for_job(mission_id, job_id):
    return any(inventory.get(f"Mission{mission_id}Job{job_id}Choice{choice_id}", False)
               for choice_id in range(1, 4))


# Funcție pentru setarea statusului unei misiuni
def set_mission_status(mission_id, status=True):
    key = f"Mission{mission_id}Complete"
    inventory[key] = status


# Functie pentru verificarea statusului unei misiuni
def check_mission_status(mission_id):
    key = f"Mission{mission_id}Complete"
    return inventory.get(key, False)

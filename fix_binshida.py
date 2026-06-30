import requests

FIREBASE_URL = "https://academic-portal-135fd-default-rtdb.firebaseio.com"

def fix_binshida():
    nodes = ["users", "active_users", "presence_v2"]
    for node in nodes:
        url = f"{FIREBASE_URL}/{node}.json"
        response = requests.get(url)
        if response.status_code != 200 or not response.json():
            continue
        
        data = response.json()
        if not isinstance(data, dict):
            continue

        for key, value in data.items():
            changed = False
            if isinstance(value, str):
                if "Binshidabinshidabinshidabinshida" in value:
                    new_val = value.replace("Binshidabinshidabinshidabinshida", "Binshidabinshid")
                    requests.put(f"{FIREBASE_URL}/{node}/{key}.json", json=new_val)
                    print(f"Updated in {node} -> {key}")
            
            elif isinstance(value, dict):
                original_name = value.get("name", "")
                if "Binshidabinshidabinshidabinshida" in original_name:
                    new_name = original_name.replace("Binshidabinshidabinshidabinshida", "Binshidabinshid")
                    value["name"] = new_name
                    requests.put(f"{FIREBASE_URL}/{node}/{key}.json", json=value)
                    print(f"Updated in {node} -> {key} name")

if __name__ == "__main__":
    fix_binshida()

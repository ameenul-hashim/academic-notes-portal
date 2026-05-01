import requests
import json

FIREBASE_URL = "https://academic-portal-135fd-default-rtdb.firebaseio.com"

def to_title_case(s):
    if not s:
        return s
    return " ".join([word.capitalize() for word in s.lower().split()])

def format_node(node_name):
    print(f"\n--- Formatting names in {node_name} ---")
    url = f"{FIREBASE_URL}/{node_name}.json"
    response = requests.get(url)
    if response.status_code != 200 or not response.json():
        print(f"No data or error fetching {node_name}: {response.status_code}")
        return

    data = response.json()
    if not isinstance(data, dict):
        return

    updates_made = 0
    for key, value in data.items():
        if isinstance(value, str):
            original = value
            new_name = to_title_case(original)
            if original != new_name:
                res = requests.put(f"{FIREBASE_URL}/{node_name}/{key}.json", json=new_name)
                if res.status_code == 200:
                    updates_made += 1
        elif isinstance(value, dict):
            original = value.get("name", value.get("username", ""))
            if original:
                new_name = to_title_case(original)
                if original != new_name:
                    value["name"] = new_name
                    # update the whole dict
                    res = requests.put(f"{FIREBASE_URL}/{node_name}/{key}.json", json=value)
                    if res.status_code == 200:
                        updates_made += 1
    
    print(f"Updates made in {node_name}: {updates_made}")

if __name__ == "__main__":
    format_node("users")
    format_node("active_users")

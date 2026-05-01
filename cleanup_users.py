import requests
import json

FIREBASE_URL = "https://academic-portal-135fd-default-rtdb.firebaseio.com"

def fetch_data(node):
    url = f"{FIREBASE_URL}/{node}.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data if isinstance(data, dict) else {}
    return {}

def main():
    users_data = fetch_data("users")
    active_users_data = fetch_data("active_users")

    print(f"Loaded {len(users_data)} from 'users' and {len(active_users_data)} from 'active_users'.")

    seen_names = {}
    to_delete = []  # List of tuples: (node_name, key)

    def process_node(node_name, data):
        for key, value in data.items():
            name = ""
            timestamp = 0
            
            if isinstance(value, str):
                name = value.strip().lower()
            elif isinstance(value, dict):
                name = value.get("name", value.get("username", "")).strip().lower()
                timestamp = value.get("time", 0)
            
            if not name:
                continue
                
            if name in seen_names:
                existing_node, existing_key, existing_time = seen_names[name]
                
                if timestamp and existing_time and timestamp < existing_time:
                    # Current one is older, delete existing
                    to_delete.append((existing_node, existing_key))
                    seen_names[name] = (node_name, key, timestamp)
                else:
                    # Existing is older or no timestamps, delete current
                    to_delete.append((node_name, key))
            else:
                seen_names[name] = (node_name, key, timestamp)

    # Process both nodes
    process_node("active_users", active_users_data)
    process_node("users", users_data)

    print(f"Total unique names: {len(seen_names)}")
    print(f"Total redundant entries to delete: {len(to_delete)}")

    for node_name, key in to_delete:
        delete_url = f"{FIREBASE_URL}/{node_name}/{key}.json"
        res = requests.delete(delete_url)
        if res.status_code == 200:
            print(f"Deleted duplicate '{key}' from '{node_name}'")
        else:
            print(f"Failed to delete {key} from {node_name}: {res.status_code}")

if __name__ == "__main__":
    main()

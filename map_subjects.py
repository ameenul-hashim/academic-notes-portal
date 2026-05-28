import os
import re

def main():
    print("Mapping files to subjects...")
    files = [f for f in os.listdir('.') if f.endswith('.html') and f != 'index.html' and not f.startswith('old_')]
    for filename in files:
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Look for the subject title in the first H1 that isn't the site title
            h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL | re.IGNORECASE)
            title = "Unknown"
            for h in h1s:
                h_cleaned = re.sub(r'<[^>]+>', '', h).strip()
                if "BA Calicut University" not in h_cleaned:
                    title = h_cleaned
                    break
            
            if title == "Unknown":
                title_match = re.search(r'<title>(.*?)</title>', content, re.DOTALL | re.IGNORECASE)
                if title_match:
                    title = title_match.group(1).split('-')[0].strip()
            
            print(f"{filename} -> {title}")
        except Exception as e:
            print(f"Error reading {filename}: {e}")

if __name__ == "__main__":
    main()

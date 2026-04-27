import re, os

# Map: filename -> correct subject name (from index.html cards)
correct_names = {
    'history': 'Philosophy of Education',
    'world': 'Philosophy of Artificial Intelligence',
    'kerala': 'English for BA Programs',
    'politics': 'Literature in Malayalam',
    'economics': 'History of Keralam upto 12th Century',
    'sociology': 'Sociology',
    'ethics': 'Fundamentals of Ethics',
    'micro-economics': 'Micro Economic Foundations',
    'philosophy': 'Development Issues in Indian Economy',
}

# Check Level 2 pages (language selection)
print("=== Level 2 (Language Selection) Pages ===")
for base, correct in correct_names.items():
    fname = f"{base}.html"
    if not os.path.exists(fname):
        continue
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', content)
    titles = re.findall(r'<title>(.*?)</title>', content)
    for h1 in h1s:
        if h1.strip() != correct:
            print(f"  MISMATCH {fname}: h1='{h1.strip()}' should be '{correct}'")
    for t in titles:
        if correct not in t:
            print(f"  MISMATCH {fname}: title='{t}' should contain '{correct}'")

# Check Level 3 pages (chapter pages)
print("\n=== Level 3 (Chapter) Pages ===")
for base, correct in correct_names.items():
    for lang in ['en', 'ml']:
        fname = f"{base}-{lang}.html"
        if not os.path.exists(fname):
            continue
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
        h1s = re.findall(r'<h1[^>]*>(.*?)</h1>', content)
        titles = re.findall(r'<title>(.*?)</title>', content)
        for h1 in h1s:
            if h1.strip() != correct:
                print(f"  MISMATCH {fname}: h1='{h1.strip()}' should be '{correct}'")
        for t in titles:
            if correct not in t:
                print(f"  MISMATCH {fname}: title='{t}' should contain '{correct}'")

print("\nDone.")

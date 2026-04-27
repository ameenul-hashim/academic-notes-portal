import re, os

# Map: filename base -> correct subject name
correct_names = {
    'history': 'Philosophy_of_Education',
    'world': 'Philosophy_of_AI',
    'kerala': 'English_for_BA',
    'politics': 'Literature_in_Malayalam',
    'economics': 'History_of_Keralam',
    'sociology': 'Sociology',
    'ethics': 'Fundamentals_of_Ethics',
    'micro-economics': 'Micro_Economics',
    'philosophy': 'Development_Issues_Indian_Economy',
}

fixed = 0

for base, subject in correct_names.items():
    for lang in ['en', 'ml']:
        fname = f"{base}-{lang}.html"
        if not os.path.exists(fname):
            continue
        
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        lang_label = 'English' if lang == 'en' else 'Malayalam'
        
        # Use a counter list to work around closure scope
        counter = [0]
        
        def fix_download(match):
            counter[0] += 1
            href = match.group(1)
            rest = match.group(2)
            filename = f"{subject}_Chapter_{counter[0]}_{lang_label}.pdf"
            return f'href="{href}" download="{filename}"{rest}'
        
        # Reset counter for each file
        counter[0] = 0
        
        # Match: href="..." download class="..." (the download links)
        content = re.sub(
            r'href="([^"]+)" download([^=])',
            fix_download,
            content
        )
        
        if content != original:
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(content)
            fixed += 1
            print(f"  Fixed: {fname}")

print(f"\nTotal files fixed: {fixed}")

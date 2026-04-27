import re, os

# Map: filename -> correct subject name
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

fixed = 0

for base, correct in correct_names.items():
    # Fix Level 2 page
    files_to_fix = [f"{base}.html", f"{base}-en.html", f"{base}-ml.html"]
    
    for fname in files_to_fix:
        if not os.path.exists(fname):
            continue
        with open(fname, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Fix all <h1> tags that contain wrong subject names
        # Find all h1 contents
        h1_matches = re.findall(r'(<h1[^>]*>)(.*?)(</h1>)', content)
        for full_open, inner, close in h1_matches:
            if inner.strip() != correct:
                content = content.replace(f"{full_open}{inner}{close}", f"{full_open}{correct}{close}")
        
        # Fix <title> tags
        lang_suffix = ""
        if fname.endswith('-en.html'):
            lang_suffix = " (English)"
        elif fname.endswith('-ml.html'):
            lang_suffix = " (Malayalam)"
        
        if lang_suffix:
            title_correct = f"{correct}{lang_suffix} - Chapters"
        else:
            title_correct = f"{correct} - Language Selection"
        
        title_match = re.search(r'<title>(.*?)</title>', content)
        if title_match and correct not in title_match.group(1):
            content = content.replace(f"<title>{title_match.group(1)}</title>", f"<title>{title_correct}</title>")
        
        # Fix mobile title (the <p> subtitle stays, just the h1 inside mobile section)
        # Already handled by the h1 replacement above
        
        if content != original:
            with open(fname, 'w', encoding='utf-8') as f:
                f.write(content)
            fixed += 1
            print(f"  Fixed: {fname} -> '{correct}'")

print(f"\nTotal files fixed: {fixed}")

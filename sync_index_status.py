import os
import re
import glob

def count_chapters(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modals = re.findall(r'id="(modal-ch\d+)"', content)
    total = len(set(modals))
    uploaded = 0
    for modal_id in set(modals):
        parts = content.split(f'id="{modal_id}"')
        if len(parts) >= 2:
            modal_content = parts[1][:2000]
            if 'drive.google.com' in modal_content or 'docs.google.com' in modal_content:
                uploaded += 1
    return total, uploaded

stats = {}
# Mapping from subject title in index.html to file prefixes
subject_map = {
    "Philosophy of Education": "history",
    "Philosophy of Artificial Intelligence": "world",
    "English for BA Programs": "kerala",
    "Literature in Malayalam": "politics",
    "History of Keralam upto 12th Century": "economics",
    "Development Issues in Indian Economy": "philosophy",
    "Sociology": "sociology",
    "Micro Economic Foundations": "micro-economics",
    "Fundamentals of Ethics": "ethics"
}

for subject, prefix in subject_map.items():
    en_file = f"{prefix}-en.html"
    ml_file = f"{prefix}-ml.html"
    
    en_total, en_uploaded = count_chapters(en_file) if os.path.exists(en_file) else (0, 0)
    ml_total, ml_uploaded = count_chapters(ml_file) if os.path.exists(ml_file) else (0, 0)
    
    stats[subject] = {
        "en": f"{en_uploaded} / {en_total}",
        "ml": f"{ml_uploaded} / {ml_total}",
        "en_status": "green" if en_uploaded > 0 else "red",
        "ml_status": "green" if ml_uploaded > 0 else "red"
    }
    # Special case: if some but not all, maybe yellow?
    if 0 < en_uploaded < en_total: stats[subject]["en_status"] = "yellow"
    if 0 < ml_uploaded < ml_total: stats[subject]["ml_status"] = "yellow"
    if en_uploaded == en_total and en_total > 0: stats[subject]["en_status"] = "green"
    if ml_uploaded == ml_total and ml_total > 0: stats[subject]["ml_status"] = "green"

# Now update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

for subject, data in stats.items():
    # Find the row for this subject
    # Pattern: Subject name followed by two columns of status spans
    pattern = re.compile(
        r'(<td[^>]*>' + re.escape(subject) + r'</td>\s*<td[^>]*>\s*<span[^>]*>)(.*?)(</span>\s*</td>\s*<td[^>]*>\s*<span[^>]*>)(.*?)(</span>)',
        re.DOTALL
    )
    
    def replacer(match):
        prefix1 = match.group(1)
        # update color in prefix1 if needed
        color_en = data["en_status"]
        prefix1 = re.sub(r'bg-\w+-500/20', f'bg-{color_en}-500/20', prefix1)
        prefix1 = re.sub(r'text-\w+-300', f'text-{color_en}-300', prefix1)
        prefix1 = re.sub(r'border-\w+-500/30', f'border-{color_en}-500/30', prefix1)
        
        mid = match.group(3)
        color_ml = data["ml_status"]
        mid = re.sub(r'bg-\w+-500/20', f'bg-{color_ml}-500/20', mid)
        mid = re.sub(r'text-\w+-300', f'text-{color_ml}-300', mid)
        mid = re.sub(r'border-\w+-500/30', f'border-{color_ml}-500/30', mid)
        
        return f"{prefix1}{data['en']}{match.group(2) if 'Uploaded' in match.group(2) else ' Uploaded'}{mid}{data['ml']}{match.group(4) if 'Uploaded' in match.group(4) else ' Uploaded'}{match.group(5)}"

    # If the span content already has "Uploaded", we don't want to duplicate it.
    # The stats[subject]["en"] is just "X / Y".
    
    def replacer_v2(match):
        # Group 1: <td>Subject</td><td><span>
        # Group 2: X / Y Uploaded
        # Group 3: </span></td><td><span>
        # Group 4: X / Y Uploaded
        # Group 5: </span>
        
        p1 = match.group(1)
        c_en = data["en_status"]
        p1 = re.sub(r'bg-\w+-500/20', f'bg-{c_en}-500/20', p1)
        p1 = re.sub(r'text-\w+-300', f'text-{c_en}-300', p1)
        p1 = re.sub(r'border-\w+-500/30', f'border-{c_en}-500/30', p1)
        
        p3 = match.group(3)
        c_ml = data["ml_status"]
        p3 = re.sub(r'bg-\w+-500/20', f'bg-{c_ml}-500/20', p3)
        p3 = re.sub(r'text-\w+-300', f'text-{c_ml}-300', p3)
        p3 = re.sub(r'border-\w+-500/30', f'border-{c_ml}-500/30', p3)
        
        return f"{p1}{data['en']} Uploaded{p3}{data['ml']} Uploaded{match.group(5)}"

    index_content = pattern.sub(replacer_v2, index_content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)

print("Updated index.html status table")

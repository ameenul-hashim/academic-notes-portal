import os
import re

# New Subject Data
new_subjects = [
    {
        "id": "ethics",
        "name": "Fundamental of Ethics",
        "en": "ethics-en.html",
        "ml": "ethics-ml.html",
        "file": "ethics.html"
    }
]

# Read Templates
with open('c:/Users/lenov/OneDrive/Desktop/pdf app/history.html', 'r', encoding='utf-8') as f:
    subject_template = f.read()

with open('c:/Users/lenov/OneDrive/Desktop/pdf app/politics-ml.html', 'r', encoding='utf-8') as f:
    language_template = f.read()

# 1. Create Subject Pages
for subj in new_subjects:
    content = subject_template
    # Update Page Title
    content = re.sub(r'<title>.*?</title>', f'<title>{subj["name"]} - Languages</title>', content)
    # Update Header Title
    content = content.replace('history of keralam upto 12th century', subj["name"].lower())
    content = content.replace('History of keralam upto 12th century', subj["name"])
    # Update Links
    content = content.replace('history-ml.html', subj["ml"])
    content = content.replace('history-en.html', subj["en"])
    
    with open(f'c:/Users/lenov/OneDrive/Desktop/pdf app/{subj["file"]}', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created {subj['file']}")

# 2. Create Language Pages (En and Ml)
for subj in new_subjects:
    for lang_code, lang_name, lang_file in [("en", "English", subj["en"]), ("ml", "Malayalam", subj["ml"])]:
        content = language_template
        # Update Page Title
        content = re.sub(r'<title>.*?</title>', f'<title>{subj["name"]} ({lang_name}) - Chapters</title>', content)
        # Update Header Title
        content = content.replace('Politics in malayalam', f'{subj["name"]} ({lang_name})')
        content = content.replace('politics in malayalam', f'{subj["name"]} ({lang_name})'.lower())
        # Update Back Link
        content = content.replace('politics.html', subj["file"])
        
        with open(f'c:/Users/lenov/OneDrive/Desktop/pdf app/{lang_file}', 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Created {lang_file}")

# 3. Update index.html
with open('c:/Users/lenov/OneDrive/Desktop/pdf app/index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Add Subject Cards
subject_cards = ""
for subj in new_subjects:
    card = f'''
            <!-- Subject Card: {subj["name"]} -->
            <a href="{subj["file"]}" class="block outline-none">
                <div class="glass-card rounded-2xl p-8 h-full flex items-center justify-center text-center transition-transform duration-300 hover:scale-105 hover:shadow-[0_0_25px_rgba(251,113,133,0.5)]">
                    <h2 class="text-2xl font-bold text-white">{subj["name"]}</h2>
                </div>
            </a>
    '''
    subject_cards += card

# Inject cards after the last subject card in the grid
# Since I added two before, I'll just append to the grid
index_content = index_content.replace('<!-- Subject Card: Micro Economics -->', '<!-- Subject Card: Micro Economics -->\n' + subject_cards)

# Add Table Rows
table_rows = ""
for subj in new_subjects:
    row = f'''
                            <tr class="hover:bg-white/5 transition-colors group">
                                <td class="py-6 px-6 font-medium group-hover:text-orange-300 transition-colors">{subj["name"]}</td>
                                <td class="py-6 px-6 text-center">
                                    <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-bold bg-red-500/20 text-red-300 border border-red-500/30">0 / 5 Uploaded</span>
                                </td>
                                <td class="py-6 px-6 text-center">
                                    <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-bold bg-red-500/20 text-red-300 border border-red-500/30">0 / 5 Uploaded</span>
                                </td>
                            </tr>
    '''
    table_rows += row

# Inject table rows at the end of <tbody>
index_content = index_content.replace('</tbody>', table_rows + '                        </tbody>')

with open('c:/Users/lenov/OneDrive/Desktop/pdf app/index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)

print("Updated index.html with Fundamental of Ethics.")

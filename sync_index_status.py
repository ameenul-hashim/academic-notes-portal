import os
import re

def count_chapters(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    modals = re.findall(r'id="(modal-ch[\d_]+|modal-discussion)"', content)
    total = len(set(modals))
    uploaded = 0
    for modal_id in set(modals):
        parts = content.split(f'id="{modal_id}"')
        if len(parts) >= 2:
            modal_content = parts[1][:2000]
            # Check for drive, docs, or supabase links, and make sure it doesn't say "Content Coming Soon"
            has_link = 'drive.google.com' in modal_content or 'docs.google.com' in modal_content or 'supabase.co' in modal_content
            has_placeholder = 'Content Coming Soon' in modal_content
            if has_link and not has_placeholder:
                uploaded += 1
    return total, uploaded

subject_map = {
    "Philosophy of Education": "history",
    "Philosophy of AI": "world",
    "English for BA Programs": "kerala",
    "Literary Malayalam": "politics",
    "History of Keralam": "economics",
    "Sociology": "sociology",
    "Micro Economics": "micro-economics",
    "Fundamentals of Ethics": "ethics",
    "Development Issues": "philosophy"
}

def make_col(stats):
    if stats is None:
        return '''<td class="py-6 px-8 text-center">
                                        <span class="text-gray-500 text-sm italic font-medium px-4">Not Applicable</span>
                                    </td>'''
    
    total, uploaded = stats
    
    if uploaded == 0:
        badge_class = "bg-red-500/10 text-red-300 border border-red-500/30 shadow-[0_0_10px_rgba(239,68,68,0.1)]"
        dot_class = "bg-red-400 animate-pulse"
    elif uploaded == total:
        badge_class = "bg-green-500/10 text-green-300 border border-green-500/30 shadow-[0_0_10px_rgba(34,197,94,0.1)]"
        dot_class = "bg-green-400"
    else:
        badge_class = "bg-yellow-500/10 text-yellow-300 border border-yellow-500/30 shadow-[0_0_10px_rgba(234,179,8,0.1)]"
        dot_class = "bg-yellow-400 animate-pulse"
        
    return f'''<td class="py-6 px-8 text-center">
                                        <span class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full text-xs font-bold {badge_class}">
                                            <span class="w-1.5 h-1.5 rounded-full {dot_class}"></span> {uploaded} / {total} Uploaded
                                        </span>
                                    </td>'''

def make_row(subject, en_stats, ml_stats):
    tr_class = 'group hover:bg-white/[0.07] transition-all duration-300'
    if subject == "Micro Economics":
        tr_class += ' border-b border-white/5'
        
    en_html = make_col(en_stats)
    ml_html = make_col(ml_stats)
    
    return f'''<tr class="{tr_class}">
                                    <td class="py-6 px-8 font-semibold text-lg group-hover:text-orange-300 transition-colors">{subject}</td>
                                    {en_html}
                                    {ml_html}
                                </tr>'''

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Update each subject row in index.html
for subject, prefix in subject_map.items():
    en_stats = count_chapters(f"{prefix}-en.html")
    ml_stats = count_chapters(f"{prefix}-ml.html")
    
    new_row = make_row(subject, en_stats, ml_stats)
    
    # Match the row using regex
    pattern = re.compile(
        r'<tr[^>]*>\s*<td[^>]*>' + re.escape(subject) + r'</td>.*?</tr>',
        re.DOTALL
    )
    
    index_content = pattern.sub(new_row, index_content)

# Write updated index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_content)

print("Successfully synchronized Academic Progress Dashboard in index.html!")

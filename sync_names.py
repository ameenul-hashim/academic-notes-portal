import os

mappings = {
    'Philosophy of Education': ['history.html', 'history-en.html', 'history-ml.html'],
    'Philosophy of Artificial Intelligence': ['world.html', 'world-en.html', 'world-ml.html'],
    'English for BA Programs': ['kerala.html', 'kerala-en.html', 'kerala-ml.html'],
    'Literature in Malayalam': ['politics.html', 'politics-en.html', 'politics-ml.html'],
    'History of Keralam upto 12th Century': ['economics.html', 'economics-en.html', 'economics-ml.html'],
    'Development Issues in Indian Economy': ['philosophy.html', 'philosophy-en.html', 'philosophy-ml.html']
}

old_names = {
    'history.html': 'History of India',
    'history-en.html': 'History of India',
    'history-ml.html': 'History of India',
    'world.html': 'World History',
    'world-en.html': 'World History',
    'world-ml.html': 'World History',
    'kerala.html': 'Kerala History',
    'kerala-en.html': 'Kerala History',
    'kerala-ml.html': 'Kerala History',
    'politics.html': 'Political Science',
    'politics-en.html': 'Political Science',
    'politics-ml.html': 'Political Science',
    'economics.html': 'Economics',
    'economics-en.html': 'Economics',
    'economics-ml.html': 'Economics',
    'philosophy.html': 'Philosophy',
    'philosophy-en.html': 'Philosophy',
    'philosophy-ml.html': 'Philosophy'
}

for new_name, files in mappings.items():
    for filename in files:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            
            old_name = old_names[filename]
            
            # Replace in title tag
            content = content.replace(f'<title>{old_name}', f'<title>{new_name}')
            # Replace in h1 tag (desktop)
            content = content.replace(f'>{old_name}</h1>', f'>{new_name}</h1>')
            # Replace in h1 tag (mobile)
            content = content.replace(f'>{old_name}</h1>', f'>{new_name}</h1>')
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {filename}")

print("Done")

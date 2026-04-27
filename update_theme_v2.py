import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html')]
new_grad = 'bg-gradient-to-br from-slate-900 via-indigo-900 to-slate-900'

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace body class
    new_content = re.sub(r'<body class="[^"]*">', f'<body class="{new_grad} min-h-screen text-white font-sans antialiased flex flex-col">', content)
    
    # Accents
    new_content = new_content.replace('text-pink-300', 'text-cyan-300')
    new_content = new_content.replace('text-pink-200', 'text-cyan-200')
    new_content = new_content.replace('text-pink-100', 'text-cyan-100')
    new_content = new_content.replace('text-pink-400', 'text-cyan-400')
    new_content = new_content.replace('from-pink-600 to-purple-700', 'from-cyan-600 to-blue-700')
    new_content = new_content.replace('focus:ring-pink-500', 'focus:ring-cyan-500')
    
    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated {f}")

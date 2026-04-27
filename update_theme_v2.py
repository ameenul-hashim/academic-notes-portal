import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html')]

# Brownish-red to light brownish-red gradient
new_grad = 'bg-gradient-to-br from-red-950 via-rose-900 to-red-800'

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace body background gradient
    new_content = re.sub(
        r'<body class="[^"]*">',
        f'<body class="{new_grad} min-h-screen text-white font-sans antialiased flex flex-col">',
        content
    )

    # Replace accent colors to match warm red theme
    new_content = new_content.replace('text-cyan-300', 'text-orange-300')
    new_content = new_content.replace('text-cyan-200', 'text-orange-200')
    new_content = new_content.replace('text-cyan-100', 'text-orange-100')
    new_content = new_content.replace('text-cyan-400', 'text-orange-400')
    new_content = new_content.replace('focus:ring-cyan-500', 'focus:ring-orange-500')
    new_content = new_content.replace('focus:ring-cyan-500/50', 'focus:ring-orange-500/50')
    new_content = new_content.replace('from-cyan-600 to-blue-700', 'from-rose-600 to-red-700')
    new_content = new_content.replace('from-blue-600 to-indigo-700', 'from-rose-600 to-red-700')
    new_content = new_content.replace('hover:from-blue-500 hover:to-indigo-600', 'hover:from-rose-500 hover:to-red-600')
    new_content = new_content.replace('focus:ring-2 focus:ring-cyan-500', 'focus:ring-2 focus:ring-orange-500')
    new_content = new_content.replace('hover:shadow-[0_0_25px_rgba(6,182,212,0.5)]', 'hover:shadow-[0_0_25px_rgba(251,113,133,0.5)]')
    new_content = new_content.replace('hover:shadow-[0_0_20px_rgba(6,182,212,0.3)]', 'hover:shadow-[0_0_20px_rgba(251,113,133,0.3)]')
    new_content = new_content.replace('bg-cyan-500/10', 'bg-rose-500/10')
    new_content = new_content.replace('text-cyan-400', 'text-rose-400')

    # Also replace any blue-themed header text
    new_content = new_content.replace('text-cyan-200 tracking-widest', 'text-orange-200 tracking-widest')

    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated {f}")

print("Done")

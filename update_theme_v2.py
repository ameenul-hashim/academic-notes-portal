import os
import re

files = [f for f in os.listdir('.') if f.endswith('.html')]

# Slightly lighter brownish-red gradient
new_grad = 'bg-gradient-to-br from-red-900 via-rose-800 to-red-700'

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace body background gradient
    new_content = re.sub(
        r'<body class="[^"]*">',
        f'<body class="{new_grad} min-h-screen text-white font-sans antialiased flex flex-col">',
        content
    )

    if new_content != content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f"Updated {f}")

print("Done")

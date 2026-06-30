import re

filepath = r'c:\Users\lenov\OneDrive\Desktop\degree main projects\pdf app\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Look for 'Academic Updates' and print the lines around it.
for m in re.finditer(r'Academic Updates', text, re.IGNORECASE):
    start = max(0, m.start() - 200)
    end = min(len(text), m.end() + 200)
    print("Found around pos", m.start())
    print("--- Context ---")
    print(text[start:end])
    print("===============")

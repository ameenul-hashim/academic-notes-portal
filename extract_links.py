import codecs
import re

with codecs.open('old_history_ml.html', 'r', 'utf-16') as f:
    content = f.read()

links = re.findall(r'href="(https://[^"]+)"', content)
for link in links:
    print(link)

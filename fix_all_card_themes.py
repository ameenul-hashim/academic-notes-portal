import os
import re

CARD_OVERRIDES = """
        /* All 14 Theme Card Overrides */
        [data-theme="rose"] .glass-card { background: rgba(255, 255, 255, 0.08) !important; border-color: rgba(255,255,255,0.2) !important; }
        [data-theme="midnight"] .glass-card { background: rgba(255, 255, 255, 0.05) !important; border-color: rgba(139, 92, 246, 0.3) !important; }
        [data-theme="ocean"] .glass-card { background: rgba(255, 255, 255, 0.05) !important; border-color: rgba(6, 182, 212, 0.3) !important; }
        [data-theme="golden"] .glass-card { background: rgba(255, 255, 255, 0.05) !important; border-color: rgba(245, 158, 11, 0.3) !important; }
        [data-theme="coffee"] .glass-card { background: rgba(255, 255, 255, 0.05) !important; border-color: rgba(120, 113, 108, 0.3) !important; }
        [data-theme="sunset"] .glass-card { background: rgba(255, 255, 255, 0.08) !important; border-color: rgba(251, 113, 133, 0.3) !important; }
        [data-theme="indigo"] .glass-card { background: rgba(255, 255, 255, 0.05) !important; border-color: rgba(99, 102, 241, 0.3) !important; }
        [data-theme="forest"] .glass-card { background: rgba(255, 255, 255, 0.05) !important; border-color: rgba(34, 197, 94, 0.3) !important; }
        [data-theme="chocolate"] .glass-card { background: rgba(255, 255, 255, 0.05) !important; border-color: rgba(120, 53, 15, 0.3) !important; }
        [data-theme="slate"] .glass-card { background: rgba(255, 255, 255, 0.05) !important; border-color: rgba(148, 163, 184, 0.3) !important; }
        [data-theme="emerald"] .glass-card { background: rgba(255, 255, 255, 0.05) !important; border-color: rgba(16, 185, 129, 0.3) !important; }
        [data-theme="dark"] .glass-card { background: rgba(255, 255, 255, 0.05) !important; border-color: rgba(255, 255, 255, 0.1) !important; }
        [data-theme="light"] .glass-card { background: rgba(255, 255, 255, 0.7) !important; border-color: rgba(0, 0, 0, 0.1) !important; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1) !important; }
        [data-theme="sky"] .glass-card { background: rgba(255, 255, 255, 0.7) !important; border-color: rgba(16, 185, 129, 0.2) !important; box-shadow: 0 10px 15px -3px rgba(16, 185, 129, 0.05) !important; }
"""

html_files = [f for f in os.listdir('c:/Users/lenov/OneDrive/Desktop/pdf app') if f.endswith('.html')]

for f in html_files:
    path = os.path.join('c:/Users/lenov/OneDrive/Desktop/pdf app', f)
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Remove existing card rules to avoid duplicates
    content = re.sub(r'\[data-theme=".*?"\] .glass-card {.*?}', '', content, flags=re.DOTALL)
    
    # Inject new card overrides before </style>
    content = content.replace('</style>', CARD_OVERRIDES + '</style>')

    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)

print("Updated glass card styles for all 14 themes.")

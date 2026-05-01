import os

script_content = """
    <script>
        // Global download fix for cross-origin Supabase links
        document.addEventListener('click', async (e) => {
            const a = e.target.closest('a[download]');
            if (a && a.href.includes('supabase.co')) {
                e.preventDefault();
                const originalText = a.innerText;
                a.innerText = 'Downloading...';
                try {
                    const response = await fetch(a.href);
                    const blob = await response.blob();
                    const url = window.URL.createObjectURL(blob);
                    const tempA = document.createElement('a');
                    tempA.href = url;
                    tempA.download = a.getAttribute('download') || 'file.pdf';
                    document.body.appendChild(tempA);
                    tempA.click();
                    document.body.removeChild(tempA);
                    window.URL.revokeObjectURL(url);
                } catch (err) {
                    console.error('Download failed', err);
                    // Fallback to opening in new tab if fetch fails (e.g. CORS)
                    window.open(a.href, '_blank');
                } finally {
                    a.innerText = originalText;
                }
            }
        });
    </script>
"""

files_to_fix = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in files_to_fix:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        try:
            with open(filename, 'r', encoding='latin-1') as f:
                content = f.read()
        except Exception as e:
            print(f"Could not read {filename}: {e}")
            continue

    if 'supabase.co' not in content:
        continue

    if 'Global download fix' in content:
        print(f"Already fixed: {filename}")
        continue
            
    if '</body>' in content:
        new_content = content.replace('</body>', script_content + '\n</body>')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed download in: {filename}")
    else:
        print(f"No </body> tag found in: {filename}")

import paka.cmark as cmark
from pathlib import Path
import subprocess

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="/assets/style.css">
</head>
<body>{}</body>
</html>
"""

OUT_DIR = Path("build/")
IN_DIR = Path("pages/")
ASSETS_DIR = Path("assets/")

def die(message):
    import sys
    print("Error:", msg, file=sys.stderr)
    sys.exit(1)

if __name__ == '__main__':

    subprocess.run(['rm', '-rf', str(OUT_DIR)], check=True)
    subprocess.run(['mkdir', str(OUT_DIR)], check=True)
    subprocess.run(['cp', '-r', str(ASSETS_DIR), str(OUT_DIR)], check=True)

    for ent in IN_DIR.iterdir():
        if not ent.is_file():
            die(f"{ent} is not a file")

        if not ent.suffix == '.md':
            continue

        cont = ent.read_text(encoding='utf-8')
        html = TEMPLATE.format(cmark.to_html(cont, safe=False, smart=True))

        out_path = (OUT_DIR / ent.name).with_suffix('.html')  
        out_path.write_text(html, encoding='utf-8')


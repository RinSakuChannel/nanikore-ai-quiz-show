from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root = Path(__file__).resolve().parent
target = root.parent / 'ナニコレ_AIクイズショー.zip'
with ZipFile(target, 'w', ZIP_DEFLATED) as z:
    for path in sorted((root / 'dist').rglob('*')):
        if path.is_file():
            z.write(path, path.relative_to(root / 'dist'))
    z.write(root / 'image-prompts.json', 'image-prompts.json')
with ZipFile(target) as z:
    assert z.testzip() is None
    assert 'index.html' in z.namelist()
    assert all(f'assets/{i:02}.png' in z.namelist() for i in range(1, 11))
    assert all(f'assets/{i:02}.webp' in z.namelist() for i in range(11, 31))
print(f'ZIP verified: {target} ({target.stat().st_size:,} bytes)')

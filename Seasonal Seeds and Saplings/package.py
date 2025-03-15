import zipfile
from pathlib import Path

source_folder = 'src/'
out_file = 'Seasonal Seeds and Saplings.zip'

def zip_dir(dir: Path | str, filename: Path | str):
    """Zip the provided directory without navigating to that directory using `pathlib` module"""
    dir = Path(dir)

    with zipfile.ZipFile(filename, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for entry in dir.rglob("*"):
            zip_file.write(entry, entry.relative_to(dir))

zip_dir(source_folder, out_file)

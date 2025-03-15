import zipfile
import os
from pathlib import Path

source_folder = 'src/'
out_file = 'Seasonal-Seeds-And-Saplings.zip'
root_folder = '[CP] Seasonal Seeds And Saplings'

def zip_dir(dir: Path | str, filename: Path | str, rootname: Path | str | None):
    """Zip the provided directory without navigating to that directory using `pathlib` module"""
    dir = Path(dir)

    with zipfile.ZipFile(filename, "w", zipfile.ZIP_DEFLATED) as zip_file:
        for entry in dir.rglob("*"):
            if rootname:
                zip_file.write(entry, os.path.join(rootname, entry.relative_to(dir)))
            else:
                zip_file.write(entry, entry.relative_to(dir))

zip_dir(source_folder, out_file, root_folder)

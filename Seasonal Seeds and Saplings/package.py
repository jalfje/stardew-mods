import os
import zipfile

source_folder = 'src/'
out_file = 'Seasonal Seeds and Saplings.zip'
    
def zipdir(path, zip_handle):
    for root, dirs, files in os.walk(path):
        for file in files:
            zip_handle.write(os.path.join(root, file), 
                             os.path.relpath(os.path.join(root, file),
                                             os.path.join(path, '..')))

with zipfile.ZipFile(out_file, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zipdir(source_folder, zipf)
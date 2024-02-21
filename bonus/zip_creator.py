import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_dir + "/" + 'compressed.zip', 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

#for testing, this code will only run if this functrion is run as a main function when called from elsewhere it will be skipped
if __name__ == "__main__":
    make_archive(filepaths=["Converter-gui.py","file-compressor.py"], dest_dir="test_dir")
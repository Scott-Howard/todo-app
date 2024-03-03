import zipfile as zp

def extract_archive(archive_path, dest_directory):
    with zp.ZipFile(archive_path, 'r') as archive:
        archive.extractall(dest_directory)

if  __name__ == "__main__":
    extract_archive(r"D:\Repos\todo-app\bonus\test_dir\compressed.zip",
                    dest_directory=r"D:\Repos\todo-app\bonus\output_dir")
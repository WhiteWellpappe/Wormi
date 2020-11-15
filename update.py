import os
import shutil

if __name__ == "__main__":
    # deleting old files and directories & copying new files and directories from share
    path = "/home/pi/Python/Wormi/"
    share = "/home/pi/share/"
    pool = os.listdir(share)
    for files in pool:
        if os.path.isfile(os.path.join(path, files)):
            try:
                os.unlink(path+files)
            except Exception:
                print(f"Deleting {files} failed.\n{Exception}" )
            try:
                shutil.copy(share+files, path)
            except Exception:
                print(f"Copying {files} failed.\n{Exception}")
    for dir in ("cogs", "pics"):
        try:
            shutil.rmtree(path+dir)
        except Exception:
            print(f"Deleting {dir} failed.\n{Exception}")
        try:
            shutil.copytree(share + dir, path + dir)
        except Exception:
            print(f"Copying {dir} failed.\n{Exception}")
    # finishing update
    print("Update finished.\nChecking for libraries.")
    try:
        # keeping libraries updated
        os.system(f"cd {path}\npip3.8 install -r requirements.txt")
    except Exception:
        print(f"requirements.txt not found or corrupted.\n{Exception}")
    try:
        print("Completed. Starting Wormi.py")
        os.system(f"cd {path}\npython3.8 {path}Wormi.py")
    except Exception:
        print(f"Wormi.py not found.\n{Exception}")

import os, shutil

if __name__=="__main__":
    path="/home/nico/Python/Wormi/"
    #deleting old files and directories
    for old in ("pairings.json", "version.txt", "Wormi.py"):       
        try:
            os.unlink(path+old)
        except:
            print(f"{old} not found.")
    for old in ("cogs", "pics"):
        try:
            shutil.rmtree(path+old)
        except:
            print(f"{old} not found")
    #copying new files and directories from share
    share="/home/nico/Windows_Share/"
    for new in ("Wormi.py", "pairings.json", "version.txt"):
        try:
            shutil.copy(share+new, path)
        except:
            print(f"Copying {new} failed.")
    for new in ("cogs", "pics"):
        try:
            shutil.copytree(share+new, path+new)
        except:
            print(f"Copying {new} failed.")
    #finishing update
    print("Update finished.\nStarting wormi.py")
    try:
        os.system("cd /home/nico/Python/Wormi/\npython3 /home/nico/Python/Wormi/Wormi.py")
    except:
        print("Wormi.py not found.")
    
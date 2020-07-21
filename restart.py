import os

if __name__=="__main__":
    print("Restarting...")
    try:
        os.system("cd /home/nico/Python/Wormi/\npython3 /home/nico/Python/Wormi/Wormi.py")
    except:
        print("Restart failed.")
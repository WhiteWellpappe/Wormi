import os

if __name__ == "__main__":
    print("Restarting...")
    try:
        os.system("cd /home/pi/Python/Wormi/\npython3.8 ./Wormi.py")
    except:
        print("Restart failed.")

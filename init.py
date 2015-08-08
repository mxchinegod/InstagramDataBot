import subprocess
import os

while True:
    direct = os.path.dirname(os.path.realpath(__file__))
    ans = raw_input("     Would you like to run the counter or read data?[C/D]: ")
    if ans == "c" or "C":
        subprocess.Popen(["python ",direct,"\InstagramBot.py"])
    else:
        subprocess.Popen(["python ",direct,"\learndata.py"])
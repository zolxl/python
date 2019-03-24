#a3.6TextProgressBar.py
import time
for i in range(101):
    print("starting...\r{:3}%".format(i),end='')
    time.sleep(0.05)
print("Done!")

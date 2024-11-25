import requests
import time

mfile = open("mfile.txt", "a")
comp = input("Enter Name: ")
rstart = input("Enter roll to start from(without 61): ")
ranstart = int(rstart)

for i in range(ranstart, 10000):
#    time.sleep(0.8)
    roll = "61" + str(i).zfill(4)
    print("\ntrying "+roll+"...")
    req = "https://old.retinabd.org/result/home/result?studentId="+roll
    res = requests.get(req)
    if comp in res.text:
        mfile.write("\n"+str(i)+". "+roll+" "+comp)
        print(str(i)+". "+roll)
        mfile.close()
        break
    else:
        continue

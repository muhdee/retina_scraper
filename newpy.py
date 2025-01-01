import requests
import time

mfile = open("mfile.txt", "a")
brcode = input("Enter Branch Code: ")
comp = input("Enter Name: ")
rstart = input("Enter roll to start from(without branch code): ")
ranstart = int(rstart)


for i in range(ranstart, 10000):
#    time.sleep(0.8)
    roll = str(brcode) + str(i).zfill(4)
    print("\ntrying "+roll+"...")
    req = "https://retinabd.org/home/result?_token=hDx7XYeJiE7ccwqaPwQjj4gDSNy4ajzt2HvSNVjr&studentId="+roll
    res = requests.get(req)
    if comp in res.text:
        mfile.write("\n"+str(i)+". "+roll+" "+comp)
        print(str(i)+". "+roll)
        mfile.close()
        break
    else:
        continue

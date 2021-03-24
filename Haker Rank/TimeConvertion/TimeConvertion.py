time=[13,14,15,16,17,18,19,20,21,22,23,12]
time1 = ["00","01","02","03","04","05","06","07","08","09",10,11,12,]
s = "06:40:03AM"
if "PM" in s:
    ns=s.replace("PM","")
    final = ns.split(":")
    print("{}:{}:{}".format(time[int(final[0])-1],final[1],final[2]))
elif "AM" in s:
    ns =s.replace("AM","")
    final = ns.split(":")
    print(final)
    if final[0]=="12":
        print("{}:{}:{}".format(00,final[1],final[2]))
    else:
        print("{}:{}:{}".format(time1[int(final[0])],final[1],final[2]))
    
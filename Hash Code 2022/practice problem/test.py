filename=["a_an_example.in.txt","b_basic.in.txt","c_coarse.in.txt","d_difficult.in.txt","e_elaborate.in.txt"]
for f in filename:
    tofin = {}
    with open(f) as file:
        data = file.read().split()
        next = 1
        for i in range(int(data[0])):
            likecount = int(data[next])
            if likecount != 0:
                for i in range(likecount):
                    next +=1
                    if data[next] in tofin:
                        tofin[data[next]] += 1
                    else:
                        tofin[data[next]] = 1
            next+=1
            dislikecount = int(data[next])
            if dislikecount !=0:
                for i in range(dislikecount):
                    next +=1
                    if len(data) != next:
                        if data[next] in tofin:
                            tofin[data[next]] -= 1
                        else:
                            tofin[data[next]] = 0
                    else:
                        break
            next+=1

    newlist = []
    for i in tofin:
        if tofin[i] > 0:
            newlist.append(i)
    newlist.insert(0,len(newlist))
    fn = f.split(".")
    file=open(fn[0],'w')
    for tof in newlist:
        file.write(str(tof)+" ")
    file.close()
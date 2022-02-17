import sys
tofin = {}
with open("c_coarse.in.txt") as file:
    data = file.read().split()
    print(data)
    next = 1
    for i in range(int(data[0])):
        likecount = int(data[next])
        print("like count",likecount)
        if likecount != 0:
            print(likecount)
            for i in range(likecount):
                next +=1
                print(data[next])
                if data[next] in tofin:
                    tofin[data[next]] += 1
                else:
                    tofin[data[next]] = 1
        next+=1
        

        dislikecount = int(data[next])
        print("dislike count",dislikecount)
        if dislikecount !=0:
            for i in range(likecount):
                next +=1
                print("next val and data",len(data), next)
                if len(data) != next:
                    print(data[next])
                    if data[next] in tofin:
                        tofin[data[next]] -= 1
                    else:
                        tofin[data[next]] = 0
                else:
                    print(tofin)
                    break
        next+=1
        print("next value",next)


newlist = []
for i in tofin:
    if tofin[i] > 0:
       newlist.append(i)
newlist.insert(0,len(newlist))
print(newlist)



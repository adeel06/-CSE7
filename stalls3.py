def leftgap(data,i):
    gap = 0
    for ele in data[i-1::-1]:
        if ele==False:
            gap+=1
        else:
            return gap
    return gap

def rightgap(data,i):
    gap=0
    for ele in data[i+1:]:
        if ele==False:
            gap+=1
        else:
            return gap
    return gap

def next_(data):
    datadict={}
    for i in range(len(data)):
        if data[i]==False:
            datadict[i]=min(leftgap(data,i),rightgap(data,i))

    index=min(datadict,key=datadict.get)
    data[index]=True
    return data

def main():
    n = int(input("Number of stalls: "))
    data=[False]*n
    for i in range(n):
        output=''
        for ele in data:
            if ele==False:
                output+='_'
            else:
                output+='X'
            print(output)

            data=next_(data)
main()


# n = int(input("Number of stalls: "))
# data = [False]*n
# datadict={}
# for i in range(len(data)):
#     if data[i]==False:
#         datadict[i]=[min(leftgap(data,i),rightgap(data,i))]

# min(datadict,key=datadict.get)
#Extra Credit

def helper(data,n):
    output=""
    for ele in range(1,n+1):
        if ele in data:
            output+="X"
        else:
            output+="_"
            #reversed to match the problem's solution from problem set
    return output[::-1]

def solve(nums):
    n = sorted(nums)
    ans = []
    for i in range(len(n)-1):
        ans.append([i,n[i+1]-n[i]])
    return max(ans,key=lambda a:a[1])


def stalls(n):
    data=[0,n+1]
    print(helper(data[1:-1],n))
    for i in range(n-len(data)+2):
        data.sort()
        index,gap=solve(data)
        data.insert(index+1,data[index]+(gap//2))
        print(helper(data[1:-1],n))


def main():
    userdata=int(input("Enter number of stalls: "))
    stalls(userdata)

main()
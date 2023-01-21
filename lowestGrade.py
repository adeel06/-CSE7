def remove_lowest(data:list):
    if len(data) < 2:
        return data
    else:
        lowest=min(data)
        data.remove(lowest)
    return data

def main():
    a = remove_lowest ( [23, 90, 47, 55, 88] )
    b = remove_lowest ( [85] )
    c = remove_lowest ( [] )
    d = remove_lowest ( [59, 92, 93, 47, 88, 47] )

    print ("a =", a)
    print ("b =", b)
    print ("c =", c)
    print ("d =", d)

main()
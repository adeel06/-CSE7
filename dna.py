def dna_errors(data1,data2):
    long_data=data1.upper() if len(data1)>=len(data2) else data2.upper()
    short_data=data1.upper() if len(data1)<len(data2) else data2.upper()
    errors=0
    #Unmatched
        #dash
    errors=errors+long_data[0:len(short_data)].count('-') + short_data.count('-')
        #does not contain- diff between len of long and short
    errors=errors+len(long_data)-len(short_data)
    #Permutations
    permutations=['AT','CG','GC','TA']

    for i in range(len(short_data)):
        data=short_data[i]+long_data[i]
        if data not in permutations  and '-' not in data:
            errors+=2
            #True and True-> True
            #False and True-> False
            #False and False-> False
            #True and False-> False

            #False or False-> False
            #True or True-> True
            #False or True-> True
            #True or False-> True
    return errors

def main():
    temp1 = "GGGA-GAATCTCTGGACT"
    temp2 = "CTCTACTTA-AGACCGGTACAGG"
    print(dna_errors(temp1,temp2))

main()
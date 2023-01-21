import re

def wordfreq():
    e = input("Enter your file name: ")
    f = open(e, 'r')
    wors=f.readlines()
    wors=[i.strip() for i in wors]
    wors=[i.split(" ")for i in wors]
    f.close()
    newwors=[]
    for i in newwors:
        for j in i:
            if "',.!?;:][-" in j:
                newwors.append(len(j-1))
            else:
                newwors.append(len(j))
            words=sum(newwors)
            z=0
            if i>13:
                z+=1
            for i in range(1,13):
                print("Proportion of {}- letter words: {}% ({} words)".format(i,round((newwors.count(i)/words)*100,2),newwors.count(i)))


           ... print("Proportion of {}- (or more) letter words: {}% ({} words)".format(13,round((z/words)*100,2),z))

wordfreq()
#     for char in ',.!?;:][-"' :
#         storage=storage.replace(char," ")
#     dbl = storage.split()
#     size = len(dbl)
#     a=b=c=d=e=f=g=h=q=j=k=l=m=n=0
#     for i in dbl:
#         if len(i)==1:
#             a = a+1
#         elif len(i)==2:
#             b = b+1
#         elif len(i)==3:
#             c = c+1
#         elif len(i)==4:
#             d=d+1
#         elif len(i)==5:
#             e=e+1
#         elif len(i)==6:
#             f=f+1
#         elif len(i)==7:
#             g=g+1
#         elif len(i)==8:
#             h=h+1
#         elif len(i)==9:
#             q=q+1
#         elif len(i)==10:
#             j=j+11
#         elif len(i)==11:
#             k=k+1
#         elif len(i)==12:
#             l=l+1
#         elif len(i)>12:
#             m=m+1

# def word_count(str):
#     counts = dict()
#     words = str.split()

#     for word in words:
#         if word in counts:
#             counts[word] += 1
#         else:
#             counts[word] = 1

#     return counts

# print(word_count('the quick brown fox jumps over the lazy dog.'))




# print("Proportion of 1-letter words:",round((a/size)*100,1),"% (",a,"words)")
# print("Proportion of 2-letter words:",round((b/size)*100,1),"% (",b,"words)")
# print("Proportion of 3-letter words:",round((c/size)*100,1),"% (",c,"words)")
# print("Proportion of 4-letter words:",round((d/size)*100,1),"% (",d,"words)")
# print("Proportion of 5-letter words:",round((e/size)*100,1),"% (",e,"words)")
# print("Proportion of 6-letter words:",round((f/size)*100,1),"% (",f,"words)")
# print("Proportion of 7-letter words:",round((g/size)*100,1),"% (",g,"words)")
# print("Proportion of 8-letter words:",round((h/size)*100,1),"% (",h,"words)")
# print("Proportion of 9-letter words:",round((q/size)*100,1),"% (",q,"words)")
# print("Proportion of 10-letter words:",round((j/size)*100,1),"% (",j,"words)")
# print("Proportion of 11-letter words:",round((k/size)*100,1),"% (",k,"words)")
# print("Proportion of 12-letter words:",round((l/size)*100,1),"% (",l,"words)")
# print("Proportion of 13(or more)-letter words:",round((m/size)*100,1),"% (",m,"words)")


# #     for i in f.readlines():
# #         t = i.replace('\n',' ')
# #         lines = lines + t.lower()
# #     for ele in lines:
# #         if ele in pun:
# #             lines = lines.replace(ele,' ')
# #     # new  = re.sub(r'[^\w\s]',' ',lines)
# #     words = lines.strip().split(' ')
# #     counts = 0
# #     dicw = counts(words)
# #     print(dicw)

# # def counts(words):
# #     counts = dict()

# #     for word in words:
# #         if word in counts:
# #             counts[word] += 1
# #         else:
# #             counts[word] = 1
# #     return counts
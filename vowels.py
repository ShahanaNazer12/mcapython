li=['hello','hi']
vowels="aeiou"
list2=[x for x in li for x in x if x in vowels]
n=print("no of vowel",len(list2))
for i in li:
    w=len(i)
    print("length of",i,"is:",w)
    if(w>=10):
        print(i,"word is",w)

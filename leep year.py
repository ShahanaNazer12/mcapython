current = int(input("Enter current year:"))
final = int(input("Enter final year:"))
if current<final:
    print("List of leap between"+str(current)+"and"+str(final)+":")
    while current < final:
        if current%4==0 and current%100!=0:
            print(current)
            if current%

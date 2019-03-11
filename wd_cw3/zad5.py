import math
def sprawdz(a1,b1,a2,b2):
    print("y = %ix + %i" % (a1,b1))
    print("y = %ix + %i" % (a2, b2))
    if(a1==a2):
        print("proste sa rownolegle")
    elif(a1*a2==-1):
        print("proste sa prostopadle")
    else:
        print("proste sa nijakie")

print(sprawdz(2,-4,2,-63))
print(sprawdz(-1, 2, 1, 3))
print(sprawdz(123,23,542,12))
a1=4

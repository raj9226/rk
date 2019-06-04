ages1 = (10,20,30,40,50,60,30)
ages2 = [10,20,30,40,50,60,30]
ages3 = {10,20,30,40,50,60,30}
print(ages1,hex(id(ages1)),type(ages1))
print(ages2,hex(id(ages2)),type(ages2))
print(ages3,hex(id(ages3)),type(ages3))
#PS:   tuple is imutable -> read only
       #list is  mutable
       #set is mutable and unorderd due to uniqueness
#read tuple
print(ages1)
print(ages1[0],hex(id(ages1[0])))
#read list
print(ages2)
print(ages2[0],hex(id(ages2[0])))

#read set
print(ages3)
       #hw:
       #how we will read in set
for x in ages3:
       print(x,hex(id(x)))
       #draw memory representation
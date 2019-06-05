#conditional statement
#where we wish to check some rules /constraints

total=500
#Regulas if-else
"""
if total>500:
    print("flat 40% off")  #PEP standard 4 spaces  are automatically leaved
else:
    print("sorry no discount")
"""
#Ladder if -else
if total>=100 and total<200:
    print("flat 20% 0ff")
elif total>=200 and total<500:
    print("flat 30 % off")
elif total>=500:
    print(" flat 50% off")
else:
    print("please add valuables of upto 100 for discounts")
    #Nested if-else
isInternetConnected =True
isGPSConnected = True
if isInternetConnected:
    print("you can browse google maps")
    if isGPSConnected:
        print("you can navigate using maps")
    else:
        print("to use navigate please switch on GPS")
else:
    print("please connect to internet")

    # use same code snippet working on Amazon/whatssap
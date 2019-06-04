johnsAge = 30
print(johnsAge,hex(id(johnsAge)))
jenniesAge =30
print(jenniesAge,hex(id(jenniesAge)))

#copy operation:Not data copy But Referrence copy
jacksAge=johnsAge
print(jacksAge,hex(id(jacksAge)))

#del johnsAge
#print(jenniesAge,hex(id(jenniesAge)))

#PS:johnAge and jennieAge are known as Referrence variable
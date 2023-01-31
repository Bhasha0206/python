val = int(input("How many lemons you have?"))
lemons = 21
if val<lemons:
    a=lemons-val
    print("You have less lemons than required = ",a)
elif val>lemons:
    b=val-lemons
    print("You have more lemons than required = ",b)
elif val<0:
    c= 0-val
    d= c+lemons
    print("You still require lemons = ",d)
else:
    print("You have required lemons")



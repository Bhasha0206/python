days=int(input("Enter the day of your plan: "))
plan=84
if (days<plan and days>0):
    calls=int(input("Enter the calls: "))
    msgs=int(input("Enter the msgs: "))
    data=float(input("Enter the data: "))
    if calls<3000:
        a=3000-calls
        print("Your remaining calls are: ",a)
    else:
        print("Your calls limit is completed")
    if msgs<100:
        b=100-msgs
        print("Your remaining msgs are: ",b)
    else:
        print("Your msgs limit is completed")
    if data<2:
        c=2-data
        print("Your remaining data is: ",c)
    else:
        print("Your data limit is completed")
else:
    print("Your data plan is expired")
email="bhasha@gmail.com"
pwd=123
otp=789456
cemail=input("Enter your email: ")
cpwd=int(input("Enter your pwd: "))
if (email==cemail and pwd==cpwd):
    cotp=int(input("Enter your otp: "))
    if cotp==otp:
        print("Login successful")
    else:
        print("Login unsuccessful due to wrong otp")
elif (email!=cemail and pwd==cpwd):
    print("Login unsuccessful wrong email")
elif (email==cemail and pwd!=cpwd):
    print("Login unsuccessful wrong pwd")
elif (email!=cemail and pwd!=cpwd):
    print("Login unsuccessful both pwd email wrong")

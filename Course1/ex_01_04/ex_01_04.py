def computepay(a,b):
    if a>40:
        rp = 40*b
        otp = (a-40)*(b*1.5)
        p = rp+otp
    else:
        p = a*b
    return (p)
hrs= input("Enter total hours:")
rate= input("Enter rate per hour:")
try:
    a = float(hrs)
    b = float(rate)
except:
    print("Please enter a numeric value")
    quit()
pay = computepay(a,b)
print ("Pay:",pay)

hrs = input("Enter Hours:")
rate = input("Enter Rate per Hour:")
fh = float(hrs)
fr = float(rate)
if fh<=40:
    tp=fh*fr
elif fh>40:
    rp=40*fr
    otp=(fh-40)*(fr*1.5)
    tp=rp+otp
print (tp)

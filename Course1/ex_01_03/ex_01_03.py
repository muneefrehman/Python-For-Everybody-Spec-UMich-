score= input("Enter Score:")
try:
    fs=float(score)
except:
    print("Please enter a numeric value")
    quit()
if fs >=1.0 or fs <0.0:
    print("Please enter value in range")
    quit()
elif fs>=0.9:
        print("A")
elif fs>=0.8:
        print("B")
elif fs>=0.7:
        print("C")
elif fs>=0.6:
        print("D")
elif fs<0.6:
        print("F")

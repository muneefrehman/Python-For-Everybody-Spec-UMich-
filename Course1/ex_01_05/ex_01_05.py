largest = None
smallest = None
while True:
    sval = input("Enter a number: ")
    if sval == "done" :
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    if largest is None:
        largest = fval
    if smallest is None:
        smallest = fval
    if fval>largest:
        largest = fval
    if fval<smallest:
        smallest = fval
large = int(largest)
small = int(smallest)
print('Maximum is',large)
print('Minimum is',small)

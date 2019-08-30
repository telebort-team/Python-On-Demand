temp = float(input("What is the current temperature now?"))

if temp > 32:
    print("Fan ON")
    print("Air Cond ON")
elif temp > 21:
    print("Fan ON")
    print("Air Cond OFF")
else:
    print("Fan OFF")
    print("Air Cond OFF")

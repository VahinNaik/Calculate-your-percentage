a = input("what did you get?: ")
b = input("out of?: ")
percentage = (float(a)/float(b))*100
if percentage<=49:
  print("you failed!! :( (F)")
elif percentage<=59:
  print("get a toutor!!(D)") 
elif percentage<=69:
  print("study harder!!(C)")
elif percentage<=79:
  print("Not good enough!!(B)")
elif percentage<=99:
  print("Good enough(A)")
elif percentage<=100:
  print("Get a life NERD!!(A+)")
else:
  print("How!!(A++)")
print(str(percentage )+ "%")
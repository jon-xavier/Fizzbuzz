n = 100

print("fizzbuzz counting up to {}".format(n))
print(" ")
for x in range(1,int(n)+1):
  if x % 3 == 0 and x % 5 == 0:
    print("fizzbuzz")
  elif x % 3 == 0:
    print("fizz")
  elif x % 5 == 0:
    print("buzz")
  else:
    print(x)
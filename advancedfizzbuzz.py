import sys

def fizzbuzz(a):
  """This function says which number it will count up to, and then it counts up to it, replacing integers divisible by 3 with the word 'fizz', divisible by 5 with the word 'buzz', and replaces them with 'fizzbuzz' if they are divisible by both"""
  
  print("fizzbuzz counting up to {}".format(a))
  print(" ")
  for x in range(1,int(a)+1):
    if x % 3 == 0 and x % 5 == 0:
      print("fizzbuzz")
    elif x % 3 == 0:
      print("fizz")
    elif x % 5 == 0:
      print("buzz")
    else:
      print(x)

if len(sys.argv) > 1:
  n = int(sys.argv[1])
elif len(sys.argv) is 1:
   try:
      n = int(input("Enter an integer to count up to: "))
   except:
     while True:
        try:
          n = int(input("That won't work. Try entering an integer: "))
        except:
          continue
        break
      
fizzbuzz(n)


#program to find factorial of a given number
def factorial (n):
  return1 if(n==1 or n==0) else n*factorial(n-1)
  num=7
  print("The factorial of",num,"is",factorial(num))
  
  
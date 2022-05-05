n=int(input("Enter number:"))
i,fact=1
s,s2=0 

try:
  if n<0:
    print("Provided number is not positive.")
 
  else:
    while i<=n:
      fact*=i
      s+=fact
      s2+=i
      i+=1
  
  print("Factorial is {0}\nSum of each step in factorial is {1}\n Sum till nth natural number is ".format(fact, s, s2))
  
except:
  print("Error")

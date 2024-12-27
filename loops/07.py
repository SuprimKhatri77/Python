while True:
 number = int(input("Enter a number b/w 1-10: "))
 if 1 <= number <= 10:
   print("gotcha")
   break 
 else: 
   print("sed try again")
   continue
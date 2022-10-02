from time import sleep

print("\n\n")

print("MM            MM       RRRRRRRRR       ")
sleep(0.8)
a = "Pri"
print("MMMM        MMMM       RRRRRRRRRR      ")
sleep(0.8)
b = "nce"
print("MM  MM    MM  MM       RR      RR      ")
sleep(0.8)
c = " Kes"
print("MM    MMMM    MM       RRRRRRRRRR      ")
sleep(0.8)
print("MM     MM     MM       RRRRRRRRR       ")
sleep(0.8)
print("MM            MM       RRRRR           ")
sleep(0.8)
print("MM            MM  ***  RR  RR      *** ")
sleep(0.8)
print("MM            MM ***** RR   RR    *****")
sleep(0.8)
print("MM            MM  ***  RR    RR    *** ")
sleep(1.1)
print("\n\n")
print("__"*20)
print("This code is created by "+a+b+c+"hri *^*")

print("Guess a no. from 0 to 10 and answers\nthe questions\n Y for yes and N for no")
print("\n\n")
boole = True
while(boole):
  while(True):
    n1 = input("Is that no. in 1,5,6,8,10 :- ")
    n1 = n1.upper()
    if n1 == "Y" or n1 == "N":
      break
#     else:
#       continue No need of continue.
  if n1 == "Y":
    t1 = 1
  else:
    t1 = 0
    
  while(True):
    n2 = input("Is that no. in 2,6,9,10 :- ")
    n2 = n2.upper()
    if n2 == "Y" or n2 == "N":
      break
#     else:
#       continue No need of continue
  if n2 == "Y":
    t2 = 2
  else:
    t2 = 0
  while(True):
    n3 = input("Is that no. in 3,6,7,8,9,10 :- ")
    n3 = n3.upper()
    if n3 == "Y" or n3 == "N":
      break
#     else:
#       continue No need of continue
  if n3 == "Y":
    t3 = 3
  else:
    t3 = 0
  while(True):
    n4 = input("Is that no. in 4,5,7,8,9,10 :- ")
    n4 = n4.upper()
    if n4 == "Y" or n4 == "N":
      break
#     else:
#       continue

  if n4 == "Y":
    t4 = 4
  else:
    t4 = 0
  mn = t1+t2+t3+t4
  print("\nIs that no. "+str(mn)) 
  while(True):
    temp = input(" Want to try again ?? \n")
    temp = temp.upper()
    if temp == "Y" or temp =="N":
      break
#     else:
#       continue no need of continue
  if temp == "Y":
    continue
  else:
    print("\n\n***Hope You Liked It....***")
    boole = False
    break

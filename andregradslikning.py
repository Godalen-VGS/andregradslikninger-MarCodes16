# Finner løsninger til alle andregradslikninger på formen ax^2+bx+c=0
import math

def losninger(a, b, c):
  diskriminanten = b**2-4*a*c
  if diskriminanten < 0:
    return "Har ingen løsning!"
  
  losning1 = (-b + math.sqrt(diskriminanten))/2*a
  losning2 = (-b - math.sqrt(diskriminanten))/2*a
  
  if diskriminanten == 0:
    return losning1
  else:
    return (losning1 , losning2)

print(losninger( 1 , 27 , 1 ))
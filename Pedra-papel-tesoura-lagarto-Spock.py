#Pedra-papel-tesoura-lagarto-Spock
c = int(input(""))

while c!= 0:
  entrada1, entrada2 = str(input("")).upper().split()
  
  if entrada1 == "TESOURA":
      if entrada2 == " PAPEL":
          print("rajesh")
      elif entrada2 == "PEDRA":
          print("sheldon")
      elif entrada2 == "LAGARTO":
          print("rajesh")
      elif entrada2 == "SPOCK":
          print ("sheldon")
          
  if entrada1 == "PAPEL":
      if entrada2 == " PEDRA":
          print("rajesh")
      elif entrada2 == "LAGARTO":
          print("rajesh")
      elif entrada2 == "SPOCK":
          print("rajesh")
      elif entrada2 == "TESOURA":
          print("sheldon")

  if entrada1 == "PEDRA":
      if entrada2 == " PAPEL":
          print("sheldon")
      elif entrada2 == "LAGARTO":
          print("rajesh")
      elif entrada2 == "SPOCK":
          print("sheldon")
      elif entrada2 == "TESOURA":
          print("rajesh")
          
  if entrada1 == "LAGARTO":
       if entrada2 == " PAPEL":
          print("rajesh")
       elif entrada2 == "PEDRA":
          print("sheldon")
       elif entrada2 == "SPOCK":
          print("rajesh")
       elif entrada2 == "TESOURA":
          print("sheldon")
          
  if entrada2 == "SPOCK":
       if entrada2 == " PAPEL":
          print("sheldon")
       elif entrada2 == "LAGARTO":
          print("sheldon")
       elif entrada2 == "PEDRA":
          print("rajesh")
       elif entrada2 == "TESOURA":
          print("rajesh")
          
  if entrada1 == entrada2 :
      print("empate")
    
  c -= 1

#my first step in Python the idea is to create strings, definition 
# of variables, if and else statements and if statements embedded  
#there is two things about our barista first he has a f-word up German 
#and he is a hardcore vegan 

print ("Grüßs Gott Mein Name ist Gunther ich bin Ihrer Barista ")
name = input("Wie heissen Sie  \n") # variable defenition
print ("ich freue mich dass "+ name+ " mit uns Heute Sind ")
carta= (" Capuccino, Verlänger und  Espresso") # variable defenition 
print ("Ich möcheten Ihnen anbieten\n" + carta +" was möchten Sie "+ name)
cliente= input()
if cliente == "Capuccino" :
    leche = input("Möchten Sie normal Milch oder Hafer  Milch  \n")
    if leche == "normal": #this is a if function embedded in another if function
        print(" es tut mir  leid wir haben keine Milch,\n wir sind ein Veganes Geschäft,  \n kein cafe für Sie Barbaric Milchtrinker")
        quit()
    else:
        print("ihrer bestelung  "+ name  + " mit Hafer milch wird in 5 minuten fertig")
if cliente == "Verlänger" :
   
      print("ihrer bestelung  "+ name + "  wird in 5 minuten fertig")
      quit()
if cliente =="Espresso" :
    print("ihrer bestelung  "+ name + "  wird in 5 minuten fertig")
    quit()
else :
    print("es tut mir leid wir haben nur"+ carta)
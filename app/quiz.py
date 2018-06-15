#ampesce19
#freestyle_project
#quiz 

import random

#a=sandwich (reliable, always there), b=ice cream sundae (sweet, crowd-pleasing), c=sushi (quirky, not for everyone), d= pizza (big personality, life of the party)  

questions=["What is your dream job?","Who is your ideal BFF?","What animal are you most like?","What city do you want to move to?","What is your ideal Friday night?","What is your favorite thing to drink?","How often do you try new foods?","Where do you like to shop?"]
a=["Accountant","Jason Bateman","Cat","Cleveland","Movie night with friends","Water","Never","Department store"]
b=["Teacher","Jennifer Aniston","Rabbit","Montreal","Dinner at your favorite spot","Wine","Occassionally","Local shops"]
c=["Artist","Russell Brand","Sloth","Tokyo","Museum event","Cosmopolitan","All the time","Trendy boutiques"]
d=["Comedian","Kevin Hart","Dog","Barcelona","Partying","Beer","If everyone else is trying it","Mall"]

atotal=0
btotal=0
ctotal=0
dtotal=0

#To-do: prompt users for each question and record results 

#Calculate winner
best_score = 0
winner = ""
if atotal > best_score:
  best_score = atotal
  winner = "a"
if btotal > best_score:
  best_score = btotal
  winner = "b"
if ctotal > best_score:
  best_score = ctotal
  winner = "c"
if dtotal > best_score:
  best_score = dtotal
  winner = "d"
winning_result = ""
winning_paragraph = ""
if winner == "a":
  winning_result = "You are a SANDWICH!"
  winning_paragraph = "You are reliable and trustworthy. Your friends couldn't get by without you!"
elif winner == "b":
  winning_result = "You are an ICE CREAM SUNDAE!"
  winning_paragraph = "You are super sweet and loveable. People turn to you when they need some cheering up."
elif winner == "c":
  winning_result = "You are SUSHI!"
  winning_paragraph = "You are edgy and trendy. Others look to you for a fun and unique adventure."
elif winner == "d":
  winning_result = "You are PIZZA!"
  winning_paragraph = "Your are the life of the party. Everyone want a piece of you!"
else:
  print ("Congrats you broke my code somehow...you're a PC...")
print (winning_result)
print (winning_paragraph)

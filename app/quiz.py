#ampesce19
#freestyle_project
#quiz

#notes on response types
##a=sandwich (reliable, always there), b=ice cream sundae (sweet, crowd-pleasing), c=sushi (quirky, not for everyone), d= pizza (big personality, life of the party)

if __name__ == "__main__":

    questions=["What is your dream job?","Who is your ideal BFF?","What animal are you most like?","What city do you want to move to?","What is your ideal Friday night?","What is your favorite thing to drink?","How often do you try new foods?","Where do you like to shop?"]
    a=["Accountant","Jason Bateman","Cat","Cleveland","Movie night with friends","Water","Never","Department store"]
    b=["Teacher","Jennifer Aniston","Rabbit","Montreal","Dinner at your favorite spot","Wine","Occassionally","Local shops"]
    c=["Artist","Russell Brand","Sloth","Tokyo","Museum event","Cosmopolitan","All the time","Trendy boutiques"]
    d=["Comedian","Kevin Hart","Dog","Barcelona","Partying","Beer","If everyone else is trying it","Mall"]

    atotal=0
    btotal=0
    ctotal=0
    dtotal=0

    def response_count():
        global atotal, btotal, ctotal, dtotal
        answers=input("Enter your answer: ")
        if answers==a or answers=="a" or answers=="A":
            atotal += 1
        elif answers==b or answers=="b" or answers=="B":
            btotal += 1
        elif answers==c or answers=="c" or answers=="C":
            ctotal += 1
        elif answers==d or answers=="d" or answers=="D":
            dtotal += 1
        else:
            print ("Error! Please enter value a-d")
            quit("Try again.")

    print ("What type of food are you based on your personality?")
    print ("Answer the following questions to find out!")
    
    #Q1
    print ("Q1:" + questions[0])
    print ("(a)" + a[0])
    print ("(b)" + b[0])
    print ("(c)" + c[0])
    print ("(d)" + d[0])
    response_count()

    #Q2
    print ("Q2:",questions[1])
    print ("(a)", a[1])
    print ("(b)", b[1])
    print ("(c)", c[1])
    print ("(d)", d[1])
    response_count()

    #Q3
    print ("Q3:",questions[2])
    print ("(a)", a[2])
    print ("(b)", b[2])
    print ("(c)", c[2])
    print ("(d)", d[2])
    response_count()

    #Q4
    print ("Q4:",questions[3])
    print ("(a)", a[3])
    print ("(b)", b[3])
    print ("(c)", c[3])
    print ("(d)", d[3])
    response_count()

    #Q5
    print ("Q5:",questions[4])
    print ("(a)", a[4])
    print ("(b)", b[4])
    print ("(c)", c[4])
    print ("(d)", d[4])
    response_count()

    #Q6
    print ("Q6:",questions[5])
    print ("(a)", a[5])
    print ("(b)", b[5])
    print ("(c)", c[5])
    print ("(d)", d[5])
    response_count()

    #Q7
    print ("Q7:",questions[6])
    print ("(a)", a[6])
    print ("(b)", b[6])
    print ("(c)", c[6])
    print ("(d)", d[6])
    response_count()

    #Q8
    print ("Q8:",questions[7])
    print ("(a)", a[7])
    print ("(b)", b[7])
    print ("(c)", c[7])
    print ("(d)", d[7])
    response_count()

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
      winning_paragraph = "Your are the life of the party. Everyone wants a piece of you!"
    else:
      print ("You are JELLO.  You fit in any mold!")
    print ("Results:")
    print ("----------")
    print (winning_result)
    print (winning_paragraph)

# Collaborators (https://www.youtube.com/watch?v=jY86KJslDmQ)
#  Megan Leich


def project():
    print("      WELCOME TO THE WEATHER WORLD ")
    print()
    print("To convert celsius to fahrenheit, Enter '1' ")
    print("To calculate average temprature, Enter '2' ")
    print("To see future weather predictions, Enter '3'")#program asks what the use wants to do
    x = input("Enter 1, 2 or 3 to continue: ")
    word1 = "1"
    while x != word1:
        print()#responds to bad input
        break
    else:
        try:
            celcius = int(input("Enter the temprature in celsius: "))
            f = (celcius*1.8)+32
            print("Temprature in fahrenheit is: ",f)#enter fahrenheit to change to celsius or vice versea
        except:
            print()
            print("Invalid Input")#responds to bad input
    word2 = "2"
    while x != word2:
        print()#responds to bad input
        break
    else:
        try:
            n = int(input("Enter how many days you wanted to be averaged: "))
            a = []
            for i in range(0,n):
                num = int(input("Enter a degree: "))
                a.append(num)
            avg = sum(a)/n#use users input to do average
            print()
            print("Average temprature of the",n ,"days is: ",round(avg,2))
        except:
            print()
            print("Invalid Input")#responds to bad input

    word3 = "3" 
    while x != word3:
        print()#responds to bad input
        break
    else:
        try:
            Z = input("Please enter a month name: ")
            A = "january"
            B = "february"
            C = "march"
            D = "april"
            E = "may"
            F = "june"
            G = "july"
            H = "august"
            I = "september"
            J = "october"
            K = "november"
            L = "december"
            if Z == A:
                from random import randint#guesses future weather
                Min = 49
                Max = 68
                number = randint(Min,Max) #the guesses are between a certain number that I got from the internet
                print("The temprature for",A,"will be around",number,"°F")#put different message for every month
                print("Have fun out there") 
            elif Z == B:
                from random import randint
                Min = 50
                Max = 70
                number = randint(Min,Max)
                print("The temprature for",B,"will be around",number,"°F")
                print("Have fun out there")     
            elif Z == C:
                from random import randint
                Min = 52
                Max = 70
                number = randint(Min,Max)
                print("The temprature for",C,"will be around",number,"°F") 
                print("Have fun out there") 
            elif Z == D:
                from random import randint
                Min = 54
                Max = 73
                number = randint(Min,Max)
                print("The temprature for",D,"will be around",number,"°F")
                print("Have fun out there")   
            elif Z == E:
                from random import randint
                Min = 58
                Max = 74
                number = randint(Min,Max)
                print("The temprature for",E,"will be around",number,"°F")
                print("Have fun out there")  
            elif Z == F:
                from random import randint
                Min = 61
                Max = 80
                number = randint(Min,Max)
                print("The temprature for",F,"will be around",number,"°F")
                print("Have fun out there")  
            elif Z == G:
                from random import randint
                Min = 65
                Max = 84
                number = randint(Min,Max)
                print("The temprature for",G,"will be around",number,"°F")
                print("Have fun out there")  
            elif Z == H:
                from random import randint
                Min = 66
                Max = 85
                number = randint(Min,Max)
                print("The temprature for",H,"will be around",number,"°F")
                print("Have fun out there")  
            elif Z == I:
                from random import randint
                Min = 65
                Max = 83
                number = randint(Min,Max)
                print("The temprature for",I,"will be around",number,"°F")
                print("Have fun out there") 
            elif Z == J:
                from random import randint
                Min = 60
                Max = 79
                number = randint(Min,Max)
                print("The temprature for",J,"will be around",number,"°F") 
                print("Have fun out there") 
            elif Z == K:
                from random import randint
                Min = 53
                Max = 73
                number = randint(Min,Max)
                print("The temprature for",K,"will be around",number,"°F")
                print("Have fun out there")  
            elif Z == L:
                from random import randint
                Min = 48
                Max = 69
                number = randint(Min,Max)
                print("The temprature for",L,"will be around",number,"°F")
                print("Have fun out there") 
            else:
                print("Invalid Input")
                print("please type month name correctly") 
        except:
            print()
            print("Invalid Input")#responds to bad input 
project()
while True:
    print()
    print("Would do you like to start again? ")
    a = input("Enter 'yes' or 'no': ")
    if a == 'yes':
        project()
    else:
        print("Thank you. Good bye")
        
        break            

            

        
            








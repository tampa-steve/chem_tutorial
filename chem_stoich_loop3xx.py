
print "****Welcome to your interactive stoichiometry problem solver.***"

while True:
    
    
    print "**You will have three attempts for the correct answer.**"
    n = 1
    while True:
        #counter = 0
        print "Attempt number = ", n,"."
        n = n + 1
        if n > 4:
            print "Sorry, no more attempts."
            exit(0)
            
        print "Insert the atomic weight of carbon (12):"
        raw_Input1 = input 
        input1 = int(input())
        print "Insert the atomic weight of oxygen(16):"
        raw_Input2 = input 
        input2 = int(input())
        x1 = input1 + input2
        print "The molecular weight of CO is:", x1
        x2 = input1 + 2*input2
        print "The molecular weight of CO2 is:", x2
        x3 = 2*input2
        print "The molecular weight of O2 is:", x3
        print "In the following reaction, calculate the mass of CO2 formed if 1.00-g of CO is available in excess oygen:"
        print "CO(g) + O2(g) ----> CO2(g)"
        print "Calculate the mass of CO2 formed. Use 2 decimal places only."
        raw_Input3 = input
        input3 = float(input())
        if input3 == 1.57:
            print "correct!"
        elif input3 != 1.57:
            print "Not correct, try again."
        print "Calculate the mass of O2 formed. Use 2 decimal places only."
        raw_Input4 = input
        input4 = float(input())
        if input4 == 0.57:
            print "correct!"
            print "Would you like to continue?"
            print "Answer with a number( 1 = yes (this problem),  2 = no, or 3 = a different problem)"
            #exit(0)
            
            #break
            #continue
        elif input4 != 0.57:
            print "Not correct."
            print "Would you like to continue?"
            print "Answer with a number (1 = yes (this problem),  2 = no, or 3 = a different problem)"
        raw_Input5 = input    
        
        input5 = int(input())
                           
        if input5 == 1:
            continue
       
        if input5 == 2:
            print "Goodbye!"
            exit(0)

        if input5 == 3:
            print "Ok. Let's try a different problem. Good luck!"
            #continue 


            print "****Welcome to your next interactive stoichiometry problem solver.***"

        while True:
    
    
                print "**You will have three attempts for the correct answer.**"
                n = 1
                while True:
        #counter = 0
            #print "Attempt number = ", n,"."
                #n = n + 1
                #if n > 4:
                    #exit(0)
            
                    print "Insert the atomic weight of sodium(23):"
                    raw_Input3 = input 
                    input3 = int(input())
                    print "Insert the atomic weight of bromine(80):"
                    raw_Input4 = input 
                    input4 = int(input())
                    x1 = input3 + input4
                    print "The molecular weight of NaBr is:", x1
                    x2 = 2*input4
                    print "The molecular weight of Br2 is:", x2
                    x3 = 2*input2
                    print "The molecular weight of O2 is:", x3
                    print "In the following reaction, calculate the mass of NaBr formed if 3.56-g of Br2 is"
                    print "available in sufficient sodium:"
                    print "Na(s) + Br2(l) ----> NaBr(s)"
                    print "Calculate the mass of NaBr formed. Use 2 decimal places only."
                    raw_Input3 = input
                    input3 = float(input())
                    if input3 == 4.58:
                        print "correct!"
                    elif input3 != 4.58:
                        print "Not correct, try again."
                    print "Calculate the mass of Na required. Use 2 decimal places only."
                    raw_Input4 = input
                    input4 = float(input())
                    if input4 == 1.02:
                        print "correct!"
                        exit(0)
                    elif input4 != 1.02:
                        print "Not correct."
                        print "Would you like to continue?"
                        print "Answer with a number (1 = yes (this problem),  2 = no, or 3 = a different problem)"
                    raw_Input5 = input    
        
                    input5 = int(input())
                           
                    if input5 == 1:
                        print "That's it for now. I hope you learned something. Goodbye!"
       
                    if input5 == 2:
                        print "Goodbye!"
                        exit(0)

                    if input5 == 3:
                        print "Ok, let's try another kind of problem. Good luck!"

    

        








    

        







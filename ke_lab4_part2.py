#ke_lab4_part2.py
# A program that computes  the annual interest rate of a set varibale using a while loop
# by: Kody Ellis



amount = 1.00
continue_ask = "yes"

while (continue_ask != "no"):

    year_counter = 0
    interest_amount = float(raw_input("Enter the annual interest rate(as a percentage)? "))
    real_interest_amount = interest_amount / 100.0
    
    amount_double = amount * 2
    
    
#Since we're returning a yearly interger, then we will say the investment 
#will double whenevr the investment goes over the double amount """    
    while (amount < amount_double):  
        amount = amount + amount*(real_interest_amount)
        year_counter += 1

    print "It will take", year_counter, "years for the investment to double."
        
    #This is to make sure that the next answer we get will eiterh be "no" or "yes"
    while(True):
        continue_ask = raw_input("Do you want to continue (put yes/no)?")
            
        if continue_ask == "yes" or continue_ask == "no":
            break
        else:
            print "I'm sorry please input either yes or no"
                

        
print "END OF SESSION. Good bye!"
        
    




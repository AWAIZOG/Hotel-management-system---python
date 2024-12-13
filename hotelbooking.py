print("\n\t\t\t\t\tWelcome to Python Hotel")
print("\nWe're glad to have you here, It's an honour to serve you, Please honour us by answering the Questions to make your experience memorable at Python Hotel\n ")
bookingtype=input("Is this a 'PRE-BOOKING' or 'ON-SPOT' ?\n").lower()
if bookingtype=='pre-booking':
    print("\npre-booking has 10% of discount")
else:
    print("OPPS!!! You just missed a chance for a discount ")

deposit=int(input("Please deposit 100000 Rs to proceed with the booking:\n"))
if(deposit==100000):
    
        print("\nAvailaible Packages")
        # print("1.Food - 1500 Rs per person")
        print("1.Room - 5000 Rs per person *excluding AC charges")
        print("2.Place Visiting - 7000 Rs per person")
        
        #ROOM CHOICE
        room_type = input("Would you like to have 'AC' room or 'Non-AC' room ? : \n").capitalize()
        num_people = int(input("How many people will stay in the room? \n"))
        room_cost = 5000 * num_people
        if room_type == "AC":
            room_cost += 2500 * num_people
        if bookingtype == "pre-booking":
            print(f"Applying 10% Early Bird discount on room cost...")
            troom = room_cost-room_cost*10/100
        
        #FOOD CHOICE
        food_choice = input("\nDo you want to order food in advance? (Yes/No): ").lower()
        if food_choice == 'yes': 
            print("\n")
            import hotelmenu
            
        #PLACES VISITING CHOICE
        place_visiting_choice = input("\nDo you want to include a place visiting package? (Yes/No): ").lower()
        place_visiting_cost =0
        if place_visiting_choice == 'yes':
            place_visiting_cost = 7000 * num_people
            
        #TOTAL EXPENSES
        total = troom + hotelmenu.ftotal + place_visiting_cost
        
        #DISPLAYING TOTAL COST AND BOOKING SUMMARY
        print("\nBOOKING SUMMARY:")
        print(f"Room Type: {room_type} Room")
        print(f"Number of People: {num_people}")
        print(f"Room Cost: {troom} Rs")
        print(f"Food Package Cost: {hotelmenu.ftotal} Rs")
        print(f"Place Visiting Cost: {place_visiting_cost} Rs")
        print("Deposited Amount: ",deposit, "Rs")
        print(f"Total Cost: {total} Rs")
        if total>deposit:
             total=total-deposit
             print("Remaining Amount to be Paid: ",total,"Rs")
        else:
             total=deposit-total
             print("Refundable Amount: ",total,"Rs")     
         
         # Final thank you message
        print("THANK YOU for choosing Python Hotel. We hope you have a wonderful stay!")
else:
    print("Please deposit the amount to proceed")
    
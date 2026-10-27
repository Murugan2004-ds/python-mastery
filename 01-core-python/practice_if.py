age=int(input("Enter your age: "))
ID_card =input("ID Card , Yes or NO : ").lower()

if age >=18 and ID_card == "yes":
    print("Entry allowed")
elif age >=18 and ID_card =="no":
    print("Come back with your ID")
else:
    print("Too young")    

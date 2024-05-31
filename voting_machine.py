count1=count2=count3=count4=0
def election():
    global count1,count2,count3,count4
    name = input("enter Your Full Name :")
    age = float(input("enter a age :"))
    if age<=18 or age>=120:
        print("Sorry you are no eligible")
    else:
        
        candidate = input("Select Your candidate ,\n VIJAYARAGHAVAN (LDF) = 1 \n VK SREEKANDAN (UDF) = 2 \n CK KRISHNAKUMAR (BJP) = 3\n")
        if(candidate=="1"):
            print("you are selected VIJAYARAGHAVAN")
            count1 = count1+1
            
        elif(candidate=="2"):
            print("you are selected VK SREEKANDAN")
            count2 = count2+1

        elif(candidate=="3"):
            print("you are selected CK KRISHNAKUMAR")
            count3 = count3+1
            
            
        else:
            print("NOTTA")
            count4=count4+1


while True:
    election()
    
    more_votes = input("Do you want to continue voting? (yes/no): ").strip().lower()
    if more_votes != "yes":
        break
    
print("--------------------------------------------------------------------------------------")
print("Final Vote Counts:")
if count1>count2 and count1>count3 and count1>count4:
    print(f"VIJAYARAGHAVAN(LDF) WIN THE ELECTION {count1} votes")
elif count2>count3 and count2>count4:
    print(f"VK SREEKANDAN(UDF) WIN THE ELECTION {count2} votes")
elif count3>count4:
     print(f"CK KRISHNAKUMAR(BJP) WIN THE ELECTION {count3} votes")
elif count4:
     print(f"NOTTA WIN THE ELECTION {count4} votes")
else:
    print("RE ELECTION / DISAPPOINTED")
print("---------------------------------------------------------------------------------------")
print("VOTES PER CANDIDATE")

print(f"VIJAYARAGHAVAN(LDF) {count1} votes")
print(f"VK SREEKANDAN(UDF) {count2} votes")
print(f"CK KRISHNAKUMAR(BJP) {count3} votes")
print(f"NOTTA {count4} votes")

    
    




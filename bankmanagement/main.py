import json
import random
import string
from pathlib import Path

class bank:
    database="data.json"
    data=[] #dummy data 
    
    try:
        if Path(database).exists():
            with open(database) as fs:
                data=json.loads(fs.read()) 
        else:
            print("no such file exists")
    except Exception as err:
        print(f"an exception occur as {err}")

    @classmethod
    def __update(cls):
        with open(cls.database,"w") as fs:
            fs.write(json.dumps(bank.data))
    @classmethod
    def __accgenerate(cls):
        alpha=random.choices(string.ascii_letters,k=3)
        nums=random.choices(string.digits,k=3)
        specialchar=random.choices("@#$%^",k=1)
        id=alpha+nums+specialchar
        random.shuffle(id)
        return"".join(id)    
    
    def Createaccount(self):
        info={
            "name": input("tell me your name: "),
            "age": int(input("enter ur age: ")),
            "email": input("tell your email: "),
            "pin": int(input("tell your pin to add: ")),
            "accountno":bank.__accgenerate(),
            "balance":0000
        }
        if info["age"]<18 or len(str(info["pin"]))!=4:
            print("sorry we cannot allow to create an acc to underage SORRY")
        else:
            print("account has been created sucessfully")
            for i in info:
                print(f"{i} : {info[i]}")
            print("please note down your acc number ")
#aba yeslai update garnu parxa update json file ma
            bank.data.append(info)

            bank.__update()


    def depositmoney(self):
        accnumber=input("please tell me your acc number: ")
        pin2=int(input("please tell your pin: "))
        userdata=[ i for i in bank.data if i["accountno"]==accnumber and i["pin"]==pin2]
        if userdata==False:
            print("no data found")
        else:
            amount=int(input("how much u want to deposit: "))
            if amount>10000 or amount<0:
                print("sorry amount derai bayo")
            else:
                print(userdata)
                userdata[0]["balance"]+=amount
                bank.__update()
                print("amount is deposited sucessfully")

    def withdraw(self):
        accnumber=input("please tell me your acc number: ")
        pin=int(input("please tell your pin: "))
        userdata = [ i for i in bank.data if i["accountno"]==accnumber and i["pin"]==pin]
        if userdata==False:
            print("no data found")
        else:
            amount=int(input("how much u want to withdraw: "))
            if amount>10000 or amount<0:
                print("sorry amount derai bayo")
            else:
                print(userdata)
                userdata[0]["balance"]-=amount
                bank.__update()
                print("amount  withdraw sucessfully")

    def details(self):
        accnumber = input("please tell me your acc number: ")
        pin = int(input("please tell your pin: "))

        for user in bank.data:
            if user["accountno"] == accnumber and user["pin"] == pin:
                print("\nYour information is:\n")
                for key, value in user.items():
                    print(f"{key}: {value}")
                return

        print("Invalid account number or pin")


    def updatedetails(self):
        accnumber = input("please tell me your acc number: ")
        pin = int(input("please tell your pin: "))

        for user in bank.data:
            if user["accountno"] == accnumber and user["pin"] == pin:

                print("You cannot change age, balance, account number")
                print("Press enter to skip any field\n")

                new_name = input("New name: ")
                new_email = input("New email: ")
                new_pin = input("New pin: ")

                if new_name != "":
                    user["name"] = new_name

                if new_email != "":
                    user["email"] = new_email

                if new_pin != "":
                    user["pin"] = int(new_pin)

                bank.__update()
                print("Bank details updated successfully")
                return

        print("No user found")

    def deleteacc(self):
        accnumber=input("please tell me your acc number: ")
        pin2=int(input("please tell your pin: "))
        userdata=[ i for i in bank.data if i["accountno"]==accnumber and i["pin"]==pin2]
        if not userdata:
            print("sorry no such data exist")

        else:
            check=input("press y for deleting or N FOR NOTHING.")
            if check=="n" or check=="N":
                pass
                print("no change")
            else:
                bank.data.remove(userdata[0])   
            print("bank acc dlt sucessfully")
            bank.__update()
user = bank()
print("press 1 for creating an account: ")
print("press 2 for depositing the money: ")
print("press 3 for withdraw the money: ")
print("press 4 for details :")
print("press 5 for updating an account: ")
print("press 6 for deleting your account: ")

check=int(input("tell your response :"))

if check == 1:
    user.Createaccount()

if check == 2:
    user.depositmoney()

if check==3:
    user.withdraw()

if check==4:
    user.details()

if check==5:
    user.updatedetails()

if check==6:
    user.deleteacc()
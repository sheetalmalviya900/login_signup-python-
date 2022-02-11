import json

print("WELCOME TO LOGIN AND SIGNUP PAGE")

def signup():
    mydata=open("userdetail.json","r")
    r = mydata.read()
    my = json.loads(r)
    for i in my:
        name=input("Enter the name : ")
        if name in my[i]["Name"]:
            print("Username is already exist in file")
            print(" TRY AGAIN ")
            break
        phone=int(input("Enter the number : "))
        pas=input("Enter the password whos first letter is in upper case,contain only 6 character,special character and number :" )
        if len(pas)==6:
            pass;
            if ("@" in pas) or ("#" in pas) or ("$" in pas) :
                pass;
                if '1' in pas or  '2' in pas or '3' in pas or '4' in pas or '5' in pas or '6' in pas or '7' in pas or '8' in pas or '9'in pas or '0' in pas :
                    pass;
                    if pas[0]>="A" and pas[0]<="Z":
                        print("STRONG PASSWORD")
                        confirmpswrd=input("Enter password one more time for confiormation ")
                        if confirmpswrd==pas:
                            print("YOUR ACCOUNT IS SUCESSFULLY CREATED")
                            dob=input("Enter the date of birth : ")
                            gender=(input("Enter the Gender : "))
                        else:
                            print("password is not same")
                    else:
                        print("Atleast add one upper case")
                else:
                    print("add one number")
            else:
                print("special character miss in password")
        else:
            print("enter the password length is 6")
        
        my[name]={"Name":name,"Number":phone,"password":pas,"Dob":dob,"Gender":gender}
    # for i in my:
        # if name in my[i]["Name"]:
        #     print("Username is already exist in file")
        #     print(" TRY AGAIN ")
        #     break
        with open("userdetail.json","w") as mydata:
            json.dump(my,mydata,indent=4)

def login():

    mydata=open("userdetail.json","r")
    r = mydata.read()
    my = json.loads(r)

    username=input(" Enter the name ")
    password=input("Enter the password")
    for i  in my:
        if username in my[i]["Name"]:
            if password in my[i]["password"]:
                print(" YOUR PAGE IS SUCESSFULLY LOGIN")
                break
            else:
                print("your password is wrong ")
                print("Try again")
        else:
            print("This username name not find in file")
            print("first signup your page")

def begin():
    option=input("what you want login or signup :")
    if option=="signup":
        signup()
    elif option=="login":
        login()
    else:
        print("Lets start with begin ")
begin()
import json
import os
import re
print("      WELCOME IN LOGIN AND SIGNUP PAGE!      ")
file=os.path.exists("signup.json")
if file ==False:
        l=[]
        with open("signup.json","a") as f:
            a=json.dump(l,f,indent=2)
            print(a)
            
user=input("what you want to do login or signup  : ")
if user=="signup":
        n=input("Enter your name : ")
        n1=input("enter your lastname : ")
        r=open("signup.json","r")
        n2=r.read()
        if n not in n2:
            print("create a strong password with a mixture of letter number and symbols")
            def pas():
                p=input("Enter your passward : ")
                if (re.search("[a-z A-Z]",p) and re.search("[0-9]",p) and (re.search("[@#$&]",p))):
                    if len(p)>=8:
                        confirm_p=input("Enter the confirm password : ")
                        if (p==confirm_p):
                            print("coorect password")     
                            dob=input("Enter your date of birth")
                            g=input("Enter your gender male or female : ")
                            gmail=input("enter your own gmail : ")    
                            print(n,"your signup is *succesfully*")
                            dic={n:{"Name":n,"Password":p,"DOB":dob,"Gender":g,"gmail":gmail}}
                            with open("signup.json","r") as f:
                                data=json.load(f)
                            data.append(dic)
                            with open("signup.json","w") as f:
                                json.dump(data,f,indent=2)
                        else:
                            print("password not mached") 
                            pas()
                            
                    else:
                        print("password must be longer than8 charater") 
                        pas()
                        
                else:
                    print("invalid password","password must be mixture of letter number and symbols")
            pas()
        else:
           print("Name is already exist")

elif user=="login":
        user_name=input("Enter your name :")
        u1=input("Enter your passward:")
        with open("signup.json","r") as f:
            da=json.load(f)
            for i in range(len(da)): 
                if da[i]["Name"]==user_name:
                    if da[i]["Password"]==u1:
                        print("*login successfully*")
                        print("your name is",da[i]["Name"],"\n")
                        print("and your data is :-\n")
                        for x,y in da[i].items():
                            print(x,'=',y)                          
                    else:
                        print("incorrect password")
                        break
                else:
                    print("Name is not exist")

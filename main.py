import json
def userdetails():
    detail={}
    new ={}
    user=input("enter the 1/2=")
    if user=="1":
        user_name=input("any name=")
   
        password1=input("enter the password1=")
        print("correct password\n pleas confirm your password")
        password2=input("enter the password2=")
        if len(password1)>=1 and len(password1)<=12:
            if "@" in password1 or "$" in password1 or "#" in password1:
                if "0" or "9" in password1:
                    if "A" or "Z" in password1:
                        if "a" or "z" in password1:
                            pass
                            # print("strong password")
                        else:
                            print("there is not small later")
                    else:
                        print("week password")
                else:
                    print("wrong password")
            else:
                print("wrong")
        else:
            print("your lenth is long")
        if password1==password2:
            # print("both are sem")
            pass
        else:
            print("both are not equal")
        
        with open("underdeatils1.json") as f:
            data=json.load(f)
        
        for i in data["userdetails"]:
            if user_name in i["name"]:
                print("user already exists")
                break
        else:
            ("signed up successfully!")

            user1=input("enter the description=")
            user2=input("enter the dob=")
            user3=input("enter the hobbies=")
            user4=input("enter the genral=")
            detail["name"]=user_name
            detail["password"]=password1
            
            
            new["description"]=user1
            new["dob"]=user2
            new["hobbies"]=user3
            new["genral"]=user4
            detail["profile"]=new
            data["userdetails"].append(detail)
        
        
            with open("underdeatils1.json","w") as f:
                json.dump(data,f,indent=2)
    elif user=="2":    
        with open("underdeatils1.json") as f:
            data=json.load(f)
        user_name=input("enter the name=")
        password1=input("enter the pasword=")
        file=open("underdeatils1.json","r")
        maindata=json.load(file)
        file.close()
        i=0
        while i<len(data["userdetails"]):
            load_data=(maindata["userdetails"][i])
            if load_data["name"] ==user_name and load_data["password"]:
                
                print(user_name,"congratulation your login is succesfull")
                print("---profile----")
                print("Username",user_name)
                print("gender",load_data["profile"]["genral"])
                print("bio",load_data["profile"]["description"])
                print("hobby",load_data["profile"]["hobbies"])
                print("dob",load_data["profile"]["dob"])
                break
            i=i+1
            print("Invalid password")
userdetails() 

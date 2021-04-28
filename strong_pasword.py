def strong_password(user_password):
    number="0123456789"
    capital_alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    small_alphabet="abcdefghijklmnopqrstuvwxyz"
    special_chrs="@#&"
    sum=0
    a=0
    x=0
    y=0
    z=0
    if len(user_password)<5 or len(user_password)>17:
        print("password length between 6 to 16")
        user_password=input("\nplease enter password")
    for i in range(len(user_password)):
        if user_password[i] in number:
            x=1
        elif user_password[i] in capital_alphabet:
            y=1
        elif user_password[i] in small_alphabet:
            a=1  
        elif user_password[i] in special_chrs:
            z=1
    sum=a+x+y+z
    if sum!=4:
        print("password must contain number,capital_alphabet,small_alphabet,apecial,")

        user_password=input("enter the correct password:\n")
    else:
        print("\ncorrect password!!")
user_password=input("enter the password")
strong_password(user_password)
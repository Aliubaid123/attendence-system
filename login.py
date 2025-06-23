'''The Second task is:
Simple Login System (3 attempts)

Store a hardcoded username/password.

Let the user try logging in up to 3 times using a loop.'''



correct_username= "ali"
correct_password= "12345"


for attempt in range(3):
    username=input("Enter the username 😎:")
    password=input("Enter the password 🤷‍♀️:")
  
    if username== correct_username and password==correct_password:
        print("login successful 👌👏")
        break
    else:
        remaining = 2 - attempt
        if remaining > 0:
            print(f"incorrect password and username🤦‍♂️ : only {remaining} attempts left")
        else:
            print("Access finished! Bye bye 🙋‍♀️")

    
    
    '''
    elif username != correct_username and password !=correct_password:
        print("incorrect username and password 🤦‍♂️: only two attempt left")
       # break
    elif username !=correct_username and password !=correct_password :
        print("incorrect username and password 🤦‍♂️ : only one attempt left")

    else:
        print("access fininshed ! bye bye 🙋‍♀️")'''


    

  
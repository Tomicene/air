# # # # x= 5
# # # # y= 13
# # # # z= x + y - x
# # # # if z > 10:
# # # #  print('good')
# # # # m= 13
# # # # if m < z:
# # # #     print('"m" is too small')
# # # # else:
# # # #   print('the value of "m" is greater than z')
# # # # if m == z:
# # # #   print('they are equals')

# # # # print("m=", m)
# # # # print("x=", x)
# # # # print("y=", y)
# # # # print("z=", "x+y-x")
# # # # print(Firstname)
# # # x= 1
# # # y= 2.99
# # # print(float(x))
# # # print(int(y))
# # text= "PythonProgramming"
# # print(text[:6])
# # print(text[-11:])

# # text= "HelloWorld"
# # print(text[-5:])
# # print(text[:5])


# # text= "abcdefg"
# # print(text[::2])
# # print(text[::-1]) 

# # text= "Negativeindexing"
# # print(text[8:13])
# # print(text[-5:])


# # text= "practicemakesprefect"
# # print(text[8:13])
# # print(text[1:19])

# # a = " Hello, World "
# # b = " Python "
# # print(a.upper())
# # print(a.lower())
# # print(a.strip())
# # print(a.lstrip())
# # print(a.rstrip())
# # print(a.replace("h", "B"))
# # print(a.split(","))

# # print(b.upper())
# # print(b.lower())
# # print(b.strip())
# # print(b.lstrip())
# # print(b.rstrip())
# # print(b.replace("y", "i")) #python to pithon
# # print(b.split("t"))
# # fruits= 20.0
# # a= "there are %d fruits in the basket" %fruits
# # print(a)


# # str= "X-DSPAM-confidence:0.8475"
# # a =(str.split(":"))
# # b= float(a[1]) 
# # c= b * 10
# # print(a)
# # print(b) 
# # print(c)

# cars = ['Mustang', 'Paghani', 'Veyron'] 
# gun = ['Ak117', 'M4A1', 'Desert Eagle']

# a = cars + gun
# b = cars * 2
# # print(a)
# # print(b)
# # print(cars)
# # print(gun)
# cars.append('Benz')
# gun.append('P90')
# print(cars)
# print(gun)

# cars = ['Mustang', 'Paghani', 'Veyron'] 
# gun = ['Ak117', 'M4A1', 'Desert Eagle']

# cars.extend(['Hummer', 'cadilac'])
# gun.extend(["Kilo14", "Ak47"])
# print(cars)
# print(gun)

# cars = ['Mustang', 'Paghani', 'Veyron'] 
# gun = ['Ak117', 'M4A1', 'Desert Eagle']
# cars.sort()
# cars.reverse()
# gun.sort()
# print(cars)
# print(gun)

# cars = ['Mustang', 'Paghani', 'Veyron'] 
# gun = ['Ak117', 'M4A1', 'Desert Eagle']
# cars.pop()
# gun.pop()
# print(cars)
# print(gun)

# cars = ['Mustang', 'Paghani', 'Veyron'] 
# gun = ['Ak117', 'M4A1', 'Desert Eagle']
# cars.remove('Veyron')
# gun.remove('Ak117')
# print(cars)
# print(gun)

# cars = ['Mustang', 'Paghani', 'Veyron'] 
# gun = ['Ak117', 'M4A1', 'Desert Eagle']

# # del cars
# # print(cars) #giving errors i think becaues the data has been deleted.
# cars.clear()
# print(cars)

# cars = ['Mustang', 'Paghani', 'Veyron'] 
# gun = ['Ak117', 'M4A1', 'Desert Eagle']
# cars.insert(2, 'Jaguar')

# print(cars)

# food =('rice', 'beans', 'meat', 'fish', 'noodles')
# dice =(2, 3, 6, 4, 5,)

# f = food[2:4]
# d = dice[2:4]

# print(f)
# print(d)
# a=input("chat>") 
# if a == "hi":
#     print("Hello, How are you.")
# elif a == "hello":
#     print("Hey buddy, how are you.")
# elif a == "Wassup":
#     print("I'm good and u?")


# age = 33

# if age >= 30:
#     print("you are old")
# else: 
#     print("you are a kid")



# i=0
# while i < 10:  
#  i += 1
#  print(i)


# while i < 11 and i > 0:
#  i -= 1
#  print(i)


# a="abcdef"

# for x in range(3):
#  x +=1
#  print(x)
 
# import random
# a = ("rock", "paper", "scissors")
# b = random.choice(a)

# c = input("play: ")
# print(b)
# if c == b:
#     print("draw")
# elif b == "rock" and c == "scissors":
#     print("rock crushes scissors, you lose")
# elif b == "scissors" and c == "paper":
#     print("scissors cuts paper, you lose")
# elif b == "paper" and c == "rock":
#     print("paper covers rock, you lose")
# elif c == "rock" and b == "scissors":
#     print("rock crushes scissors, you win")
# elif c == "scissors" and b == "paper":
#     print("scissors cuts paper, you win")
# elif c == "paper" and b == "rock":
#     print("paper covers rock, you win")
# else:
#     print("Invalid input")
# a= input("name: ")
# def you(name):
#  print(f"I am {name}!")
#  pass
# you(a)
# b = input("number of reptition: ")
# a = int(b)
# c = " Happy new year"
# print(c * a)

# def log():
#     a = input("input a number: ")
#     d = int(a)
#     b = d**2
#     c = b/2
#     print(c)

# log()


# a = input("input the number children you have: ")
# i = int(a)
# b=[]
# def perform():
#     for x in range(i):
#         c = input("name: ")
#         b.append(c)
#         print(b)

# perform()

# def nameCard(fname, lname):
#     print("Name: "+fname + " " + lname)

# nameCard(lname = 'adams', fname = 'tunde')    

# db = {
#     'Bode001': '12345',
#     'Tomicene': 'a1234b',
#     'NIIT' : 'pass123'
# }
# username = input('Please, enter your Username: ')
# if username in db.keys():
#     nopassword = True
#     while nopassword:
#         password = input("Input password: ")
#         if db[username] == password:
#             nopassword= False
#             print("Welcome, " + username)
# else: 
#     wrongun = True
#     while wrongun:
#         print('Invalid, Username enter a valid Username to continue')            
#         username = input('Please, enter your Username: ')
#         if username in db.keys():
#             wrongun = False
                    
                    
                    
            
# db = {
#     'Bode001': '12345',
#     'Tomicene': 'a1234b',
#     'NIIT' : 'pass123'
# }
    
# def up():
#     for user in db.keys():
#         db[user.upper()]=db.pop(user)
    
# def login():
#     up()
#     i = 0
#     print('LOGIN')
#     username = input('Please, enter your Username: ').upper()
#     while username not in db.keys():
#         print('Invalid Username, enter a valid Username to continue')            
#         username = input('Please, enter your Username: ').upper()

#     else:    
#         if i ==0:
#             print('''
#                   You have three trials to input your password
#                   Else your account would be blocked.
#                   ''')
#             password = input("Input password: ")
#             i += 1
#             if db[username] == password:
#                 print("welcome " + username)
#             elif i==1:
#                 password = input("2 tries left , Input password: ")
#                 if db[username] == password:
#                     print("welcome " + username)
#                 else:
#                     password = input("last trial , Input password: ")
#                     if db[username] == password:
#                         print("welcome " + username)
#                     else:
#                         res=input(username + "YOUR ACCOUNT HAS BEEN SUSPENDED \n do you want to restart?")
#                         if res == 'y':
#                             login()
#                         elif res == 'n':
#                             print("GOOD BYE ('_')")  
                            
# def signup():
#     print('SIGN-UP')
#     newuser = input('Chose a username: ')
#     if newuser not in db.keys():
#         print('Username available')
#         newpass = input(newuser + ' input a password: ')
#         plenght= len(newpass)
#         while plenght < 4:
#             newpass = input(newuser + ' input a password(atleast 4 characters): ')
#         else:
#             db[newuser] = newpass
#             print(db)
#             login()
        
#     else:
#         ask1 = input('''username existing do you want to login or create new account? 
#         1. login
#         2. create new account 
#         >>>''')
#         if ask1 == '1':
#             login()
#         elif ask1 == '2':
#             signup()

# def main():
#     print("WELCOME TO MY WEBSITE")         
#     ask = input("do you have an account \n (y/n)")
#     winput = True
#     if ask == "y":
#         login()
#     elif ask == 'n':
#         signup()
#     else:
#         while winput:
#             print('invalid input, Input y/n')
#             ask = input(">>>")
#             if ask == "y":
#                 winput = False
#                 login()
#             elif ask ==1n':
#                 signup()
#                 winput = False
#             else:
#                 winput = True
                
                
# main()     
db = {
    'BODE001': '12345',
    'TOMICENE': 'a1234b',
    'NIIT': 'pass123'
}

def login():
    print('LOGIN')
    username = input('Please, enter your Username: ').upper()
    if username not in db:
        print('Invalid Username. Please sign up first.')
        return

    print('You have three trials to input your password.')
    for attempt in range(1, 4):
        password = input(f"Attempt {attempt}/3 - Input password: ")
        if db[username] == password:
            print(f"Welcome, {username}!")
            return
        print("Incorrect password.")
    
    print(f"{username}, your account has been suspended.")
    restart = input("Do you want to restart? (y/n): ").lower()
    if restart == 'y':
        main()

def signup():
    print('SIGN-UP')
    newuser = input('Choose a username: ').upper()
    if newuser in db:
        print("Username already exists. Please log in.")
        login()
        return
    
    while True:
        newpass = input(f"{newuser}, input a password (at least 4 characters): ")
        if len(newpass) >= 4:
            db[newuser] = newpass
            print("Account created successfully!")
            login()
            return
        print("Password too short. Try again.")

def main():
    print("WELCOME TO MY WEBSITE")
    while True:
        ask = input("Do you have an account? (y/n): ").lower()
        if ask == 'y':
            login()
            return
        elif ask == 'n':
            signup()
            return
        print("Invalid input. Please enter 'y' or 'n'.")

main()

# x = lambda a, b : a * b
# print(x(5 , 6))

# def func(n):
#     return lambda a : a * n

# mydblr = func(2)

# print(mydblr(16))    


# class myclass:
#     x = 5
#     y =10

# print(myclass.x)



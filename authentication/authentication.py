def signup():
    data = open('data.txt', 'r')
    Username = input('Create username\n')
    Password = input('Create password\n')
    PasswordC = input('Confirm password\n')

    d = []
    f = []
    for i in data:
        a,b = i.split(", ")
        b = b.strip()
        d.append(a)
        f.append(b)
    dd = dict(zip(d, f))
    # print(dd)

    if Password != PasswordC:
        print("xx Passwords don't match!\n")
        signup()
    else:
        if len(Password) < 8:
            print('xx Password length less than 8 characters\n')
            signup()
        elif Username in d:
            print('xx Username exists')
            signup()
        else:
            db = open('data.txt', 'a')
            db.write(Username+', '+Password+'\n')
            print('>> Success!\n')

def login():
    data = open('data.txt', 'r')
    Username = input('Enter username\n')
    Password = input('Enter password\n')

    if not len(Username or Password) < 1:
        d = []
        f = []
        for i in data:
            a,b = i.split(", ")
            b = b.strip()
            d.append(a)
            f.append(b)
        dd = dict(zip(d, f))

        try:
            if dd[Username]:
                try:
                    if Password == dd[Username]:
                        print('>> Login success\n')
                        print('welcome back '+Username)
                    else:
                        print('xx Password or Username incorrect\n')
                except:
                    print('xx Password or Username incorrect\n')
            else:
                print("xx Username doesn't exist\n")
        except:
            print("xx Password or Username doesn't exist\n")
    else:
        print('Enter a value')
        login()

def home(option=None):
    option = input('1-Login | 2-Signup\n')
    if option == '1':
        login()
    elif option == '2':
        signup()
    else:
        print('Invalid input')
        home()
home()
import string
import random

def randomize(option, length):
    # Options:
    #       -p      for letters, numbers and symbols
    #       -l      for letters only
    #       -n      for numbers only
    #       -m      for month selection
    #       -d      for day selection
    #       -y      for year selection
    #       -g      for gender

    if option == '-p':
        string._characters_='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+'
    elif option == '-l':
        string._characters_='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    elif option == '-n':
        string._characters_='1234567890'


    if option == '-d':
        _generated_info_=random.randint(1,28)
    elif option == '-m':
        _generated_info_=random.randint(1,12)
    elif option == '-y':
        _generated_info_=random.randint(1950,2000)
    elif option == '-g':
        _generated_info_=random.randint(1,3)
    else:
        _generated_info_=''
        for _counter_ in range(0,length) :
            _generated_info_= _generated_info_ + random.choice(string._characters_)

    return _generated_info_

def generate_user_info(arabic_name):
    firstname = arabic_name['first_name']
    lastname = arabic_name['last_name']
    username= str.lower(randomize('-l',10)) + randomize('-n',4) 
    password= randomize('-p',16)
    month= randomize('-m',1)
    day= randomize('-d',1)
    year= randomize('-y',1)
    gender= randomize('-g',1)
    
    dob = {
        'month': month,
        'day': day,
        'year': year
    }
    user = {
        'firstname': firstname,
        'lastname': lastname,
        'username': username,
        'password': password,
        'gender': gender,
        'dob': dob
    }
    return user
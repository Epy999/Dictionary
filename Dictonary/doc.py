import json
import numpy as np
import textwrap

file_path = "doc.json"

def get_dict(arr ) :
    for row in arr :
        for _val in row:
            if _val != None:
                print(f"\033[1;4;34m{_val.get('word').title()}\033[0m : \033[34m{_val.get('meaning')}\033[0m ")


def get_letter( arr,let):
    for row in arr :
        for _val in row:
            if _val != None:
                if _val.get('word')[0].lower()==let.lower():
                    print(f"\033[1;4;34m{_val.get('word').title()[0]}\033[0m\033[1;34m{_val.get('word')[1:len(_val.get('word'))]}\033[0m : \033[34m{_val.get('meaning')}\033[0m ")


def get_meaning(arr,let):
    Meaning=True
    for row in arr :
        for _val in row:
            if _val != None:
                if _val.get('word').lower()==let.lower():
                    print(f"\033[1;4;34m{_val.get('word').title()}\033[0m : \033[34m{_val.get('meaning')}\033[0m ")
                    Meaning=False
    
    if Meaning:
        i=len(let)+1
        while i > 0:
            i -= 1
            for row in arr :
                for _val in row:
                    if _val != None:
                        if i==0:
                            if _val.get('word')[i].lower()==let.lower()[i]:
                                
                                print(f"\033[1;4;34m{_val.get('word').title()}\033[0m : \033[34m{_val.get('meaning')}\033[0m ")
                                arr = [
                                        [d for d in sublist if d != _val]  
                                        for sublist in arr
                                                ]
                        if i> 0:
                            if _val.get('word')[0:i].lower()==let[0:i].lower():
                                print(f"\033[1;4;34m{_val.get('word').title()[0:i]}\033[0m\033[1;34m{_val.get('word')[i:len(_val.get('word'))]}\033[0m : \033[34m{_val.get('meaning')}\033[0m ")
                                arr = [
                                        [d for d in sublist if d != _val]  
                                        for sublist in arr
                                                ]
                        
def get_info():
    info={
        'Creator': 'Akash Ranjan',
        'Github': 'AudiXXXX',
        'Discord' : 'Audi_Py',
        'Email': 'aakshranjan5d@gmail.com'
    }
    for key, value in info.items():
        print(f"\033[1;4;33m{key}\033[0m : \033[33m{value}\033[0m")

def get_help():
    text='Enter word and know its meaning. \nEnter Letter for finding word. \nEnter --d for dictionary.   \nEnter --h for help. \nEnter --i for information about text. \nEnter exit() for exit  '
    print(f"\033[34m{text}\033[0m")

def instruction():
    print('\t\t',"\033[1;4;31m Oxford Dictionary \033[0m")
    text='Welcome to our new dictionary. This dictionary is only for you and we develop it to help you.'
    text= textwrap.fill(text, 20+16+16+4)
    print(f"\033[32m{text}\033[0m")
    text='Enter word and know its meaning. \nEnter Letter for finding word. \nEnter --d for dictionary.   \nEnter --h for help. \nEnter --i for information about text. \nEnter exit() for exit  '
    print(f"\033[32m{text}\033[0m")
    


def manger( dict_ : dict):
    instruction()
    dictionary= dict_
    array = np.empty((26,20),dtype=object)
    i=0
    j=0
    for _val in dictionary.get('Word'):
        array[i][j]= _val
        if j==19:
            i +=1
            j = -1
        j +=1
    while True:
        input_ = input('\033[31m>>>\033[0m').lower()
        if input_==  'exit()':
            print("\033[31mExiting...\033[0m")
            break
        elif len(input_) == 1:
            get_letter(array,input_)
        elif input_ == '--d':
            get_dict(array)
        elif input_ == '--i':
            get_info()
        elif input_ == '--h':
            get_help()
        else:
            get_meaning(array,input_)



    






try:
    with open(file_path, "r") as file:
        dict_ = json.load(file)
        manger(dict_)
except Exception as e:
    print(f"An error occurred: {e}")



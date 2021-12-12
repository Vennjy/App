
import os

loop = True
escape = {'no', 'x', 'break', 'quit', 'exit', 'goodbye'}  # Keys to break the loop
stuff = []  # The list


def create():  # For creating an element in the list
    a = input('what do you want to add? ')

    for thing in a.split(', '):
        stuff.append(thing)
    print(f'{stuff}\n')


def remove():  # For removing an element in the list
    a = input('what do you want to remove? ')

    for thing in a.split(', '):
        if thing not in stuff:
            print(f'{thing} does not exist :P')
        else:
            stuff.remove(thing)
            print(f'{stuff}\n')


def save(lisht):  # For saving the list
    collection = {*lisht}
    with open('Stuff.txt', 'w') as txt:
        for item in sorted(collection):
            txt.write(f'{item},')


# __[ Loop ]__

# First checking if there is already existing list in Stuff.txt -- if so, then stuff == each element in Stuff.txt

if os.path.isfile('Stuff.txt'):
    with open('Stuff.txt', 'r') as file:
        stuff = [x for x in file.read().split(',') if x != '']

while loop:  # The main loop

    ask = input('>>> ')
    x = ask.lower()
    condition = x in escape
    if condition:
        print('Ok Goodbye :)')
        break

    else:
        if x == 'create':
            create()

        elif x == 'remove':
            remove()

        elif x == 'show':
            if not stuff:
                print('List is empty')
            else:
                print(stuff)

    save(stuff)

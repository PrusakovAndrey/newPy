import json
from reading import *

def mainMenu():
    print("Выбирите желаемое действие:\n1) Создать заметку\n2) Корректировать заметку\n3) Удалить заметку\n4) Вывести на экран список всех заметок\n5) Вывести заметки с фильтрацией")
    a = int(input("- > "))
    match a:
        case 1:
            newNote('notes.txt')
        case 2:
            correctionNote('notes.txt')
            print ("для продолжения нажмите Y, для прекращения любую клавишу")
            u = input ("- > ")
            if u != 'Y':
                print('ok')
            else:
                mainMenu()
        case 3:
            deleteNote('notes.txt')
        case 4:
            printListOfNotes('notes.txt')
            print ("для продолжения нажмите Y, для прекращения любую клавишу")
            u = input ("- > ")
            if u != 'Y':
                print('ok')
            else:
                mainMenu()
        case 5:
            printSelectedNotes('notes.txt')
        case _:
            print ("выбор не сделан")

mainMenu()

print ("для продолжения нажмите Y, для прекращения любую клавишу")
u = input ("- > ")
if u != 'Y':
    print('ok')
    exit
else:
    mainMenu()



import json
import datetime


# сохранение данных в файл
def newNote (existFile):
    try:
        temp = json.load(open(existFile))
    except:
        temp = []
    title = input("Введите заголовк заметки -> ")
    body = input("Введите тело заметки -> ")
    date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    temp.append({
            "id": len(temp)+1,
            "title": title,
            "body": body,
            "date": date
        })
    with open (existFile, 'w') as file:
        json.dump(temp, file, indent=2, ensure_ascii=False)


# вывод спсика всех заметок
def printListOfNotes (infile):
    with open(infile) as file:
        tempData = json.load(file)
        for elem in tempData:
            print('{0}: {1}'.format(elem['id'],elem['title']))

# вывод заметки или заметок по одному из двух критериев (идентификатор или тема)
def printSelectedNotes (infile):
    print ("По какому критерию отфильтровать заметки?\nПо идентификатору = 1\nПо названию = 2\nСделайте выбор")
    userChoice = input()
    
    with open(infile) as file:
        tempData = json.load(file)

    if userChoice == '1':
        x = input ("Введите id заметки -> " )
        for elem in tempData:
            if elem['id'] == int(x):
                print('Заметка № {0}: Название {1}: \nСодержание - {2}'.format(elem['id'],elem['title'],elem['body']))
    if userChoice == '2':
        x = input ("Введите назавание заметки -> " )
        for elem in tempData:
            if elem['title'] == x:
                print('\nЗаметка № {0}: Название {1}: \nСодержание - {2}'.format(elem['id'],elem['title'],elem['body']))

# printListOfNotes('notes.txt')
# printSelectedNotes('notes.txt')
# newNote('notes.txt')

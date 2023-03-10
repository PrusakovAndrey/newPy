import json
import datetime

# редактирование заметки
# по заданным параметрам находим заметку и меняем содержание
def correctionNote (file):
    try:
        temp = json.load(open(file))
    except:
        print ("Нечего корректировать, нет ни одной заметки")
    for elem in temp:
        print('{0}: {1}_{2}'.format(elem['id'],elem['title'],elem['body']))
    noteNumber = int(input ("\nВведите номер заметки, которую хотите скорректировать -> "))
    
    for item in temp:
            if item['id'] == noteNumber:
                print("\n",item['title']," _ ",item['body'])
                selectedPart = input ("Выберите что необходимо скорректировать: \n1 - Название\n2 - Cодержание\n- > ")
                if selectedPart == '1':
                    newTitle = input("Новое название: ")
                    item.update({'title':newTitle})
                if selectedPart == '2':
                    newBody = input("Новое содержание заметки: ")
                    item.update({'body':newBody})
                with open (file, 'w') as file:
                    json.dump(temp, file, indent=2, ensure_ascii=False)
            else:
                print ('Заметка не найдена')

# создание новой заметки
def newNote (existFile):
    try:
        temp = json.load(open(existFile))
    except:
        temp = []
    title = input("Введите заголовк заметки -> ")
    body = input("Введите тело заметки -> ")
    date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
    temp.append({
            "id": ixForNewNote(existFile),
            "title": title,
            "body": body,
            "date": date
        })
    with open (existFile, 'w') as file:
        json.dump(temp, file, indent=2, ensure_ascii=False)

# вывод списка всех заметок
def printListOfNotes (infile):
    with open(infile) as file:
        tempData = json.load(file)
        for elem in tempData:
            print('{0}: {1}'.format(elem['id'],elem['title']))

# вывод заметки или заметок по одному из двух критериев (идентификатор, тема или дата)
def printSelectedNotes (infile):
    print ("По какому критерию отфильтровать заметки?\nПо идентификатору = 1\nПо названию = 2\nПо дате = 3\nСделайте выбор")
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
    if userChoice == '3':
        x = input ("Введите  дату в формате (ДД-ММ-ГГГГ) -> " )
        for elem in tempData:
            if elem['date'][:10] == x:
                print('\nЗаметка № {0}: Название {1}: \nСодержание - {2}'.format(elem['id'],elem['title'],elem['body']))

# модуль удаления заметки
def deleteNote (file):
    userChoice = int(input("Выберите id заметки на удаление - > "))
    with open(file, 'r') as f:
        temp = json.load(f)
        minimal = 0
        for item in temp:
            if item['id'] == userChoice:
                temp.pop(minimal)
            else:
                None
            minimal = minimal + 1

        with open(file, 'w') as outfile:
            json.dump(temp, outfile, indent=2, ensure_ascii=False)

# определение индекса, сначала ищем максимальный идентификатор заметки среди имеющихся и добавляем к нему 1
def ixForNewNote(file):
    try:
        temp = json.load(open(file))
    except:
        temp = []
    list = []
    for items in temp:
        list.append(items['id'])
    return max(list)+1

# print (ixForNewNote('notes.txt'))
# printListOfNotes('notes.txt')
# printSelectedNotes('notes.txt')
# newNote('notes.txt')
# correctionNote('notes.txt')
# deleteNote('notes.txt')

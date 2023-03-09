import datetime
import json
from turtle import title


class Note:
    def __init__(self, id, title, body, creationDate, upDate):
        self.id = id
        self.title = title
        self.body = body
        self.creationDate = creationDate
        self.upDate = upDate

    def __str__(self):
#        return f"ID: {self.id} \nНазвание: {self.title} \nЗаметка: {self.body} \nДата создания: {self.creationDate} \nДата обновления: {self.upDate}"
        note = {
            "ID": self.id,
            "Название": self.title,
            "Заметка": self.body,
            "Дата создания": self.creationDate,
            "Дата обновления": self.upDate
            }
        return note

a = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

first = Note('1','Memories', 'jnvekhbjeqv', '2022', 'a')
second = Note(2,'toDo', 'njkcwqnvlqwk niowevlk opkwl; m;', 2022, a)

#print(first)

note1 = {
    'id':1,
    'title': 'Memories',
    'body': 'jnvekhbjeqv'
    }

def write_json(note1):
    try:
        data = json.load(open('data.txt'))
    except:
        data = []
    data.append(note1)
    with open ('data.txt', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


write_json(note1)
import datetime
import json


class Note:
    def __init__(self, id, title, body, creationDate, upDate):
        self.id = id
        self.title = title
        self.body = body
        self.creationDate = creationDate
        self.upDate = upDate

    #def display_info(self):
    #    print(f"ID: {self.id} Название {self.title} Заметка {self.body} Дата создания {self.creationDate} Дата обновления {self.upDate}")

    def __str__(self):
        return f"ID: {self.id} \nНазвание: {self.title} \nЗаметка: {self.body} \nДата создания: {self.creationDate} \nДата обновления: {self.upDate}"

a = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")

first = Note(1,'Memories', 'jnvekhbjeqv', 2022, a)
second = Note(2,'toDo', 'njkcwqnvlqwk niowevlk opkwl; m;', 2022, a)

print(first,second) 

with open ('data.txt', 'w') as outfile:
    json.dump(Note. outfile)
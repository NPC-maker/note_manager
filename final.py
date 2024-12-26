# Grade 1 Этап 1 Задание 5
username=input("Введите имя: ")
title=input("Название заметки: ")
content=input("Описание заметки: ")
content2=input("")
content3=input("")
content4=input("")
full_content=[
    content2,
    content3,
    content4
]
status=input("Статус выполнения: ")
created_date=input("Дата создания: ")
issue_date=input("Дедлайн: ")
note=[username,
      title,content,
      [content2,content3,content4],
      status,
      created_date[0:5],
      issue_date[0:5]
      ]
print("Имя:",username)
print("Название заметки:",title)
print("Описание заметки:",content)
print(full_content)
print("Статус выполнения:",status)
print("Дата создания заметки:",created_date[0:5])
print("Дедлайн:",issue_date[0:5])
print(note)
import sqlite3

connection = sqlite3.connect("web.db")
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS workers (
    id INTEGER PRIMARY KEY,
    fio TEXT NOT NULL,
    gender TEXT NOT NULL,
    job_title TEXT NOT NULL,
    work_time  INTEGER NOT NULL,
    city TEXT NOT NULL,
    key_skills TEXT NOT NULL,        
    cv_link TEXT NOT NULL
    )
''')
cursor.execute('''INSERT INTO workers (fio, gender, job_title, work_time, city, key_skills, cv_link) VALUES 
               ("Иванов Иван Иванович", "муж", "Инженер", "3", "Казань", "Linux, Windows, Vmware", "https://hh.link/cv/11"), 
               ("Иванов Анатолий Иванович", "муж", "Строитель", "2", "Москва", "Кладка, Крыши", "https://hh.link/cv/12"),
               ("Иванова Елена", "жен", "Дизайнер", "1", "Нижний Новгород", "Проект модельной одежды, Проект комнат", "https://hh.link/cv/13"),
               ("Алексеева Екатерина Ильина", "жен", "Повар", "6", "Санкт-Петербург", "Французская кухня, Итальянская кухня", "https://hh.link/cv/14"), 
               ("Сергеев Максим Семенович", "муж", "Программист", "8", "Екатеринбург", "Python", "https://hh.link/cv/15"),
               ("Лисина Ольга Олеговна", "жен", "Консультант", "4", "Сахалин", "Техника, Посуды", "https://hh.link/cv/16"),
               ("Волкова Елизавета Максимовна", "жен", "Экономист", "2", "Елабуга", "Фондовый рынок", "https://hh.link/cv/17"),
               ("Синицин Роман Романович", "муж", "Аналитик", "3", "Нижнекамск", "Аналитика стоимости квартир", "https://hh.link/cv/18"),
               ("Лисова Любава Петровна", "жен", "Продавец", "2", "Набережные Челны", "Опыт в Пятерочке", "https://hh.link/cv/19"),
               ("Медведева Рита Семеновна", "жен", "Медсестра", "1", "Казань", "Операционный отдел", "https://hh.link/cv/20")''')

connection.commit()
connection.close()
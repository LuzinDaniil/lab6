#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(
 host="127.0.0.1",
 user="python",
 passwd="django",
 db="python",
 charset="utf8"
)
cursor = db.cursor(MySQLdb.cursors.DictCursor)
cursor.execute("""INSERT INTO Books
 (name, author, description)
 VALUES
 (%s, %s, %s),
 (%s, %s, %s)""",
 ("Война и Мир", "Лев Толстой", "Классика",
 "Буря мечей", "Джордж Мартин", "Топ")
 )
db.commit()
cursor.execute("SELECT * FROM Books")
books = cursor.fetchall()
print(books)
for book in books:
 print("{}: {} {} {}".format(book['id'],
 book['name'],
 book['author'],
 book['description']
 ))
cursor.execute("DELETE FROM Books WHERE id>1")
db.commit()
cursor.close()
db.close()

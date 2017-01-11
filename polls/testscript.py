import MySQLdb

db = MySQLdb.connect(
    host="127.0.0.1",
    user="root",
    passwd="1996",
    db="first_db",
    charset="utf8"
)

c = db.cursor()

c.execute("INSERT INTO books (name, description) values (%s,%s);", ('Книга', 'Описание книги'))

db.commit()
c.execute("SELECT * FROM books;")
entries = c.fetchall()
for e in entries:
    print(e)
c.close()
db.close()

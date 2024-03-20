import MySQLdb

connection = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="password", db="cool_db", charset="utf8")
cursor = connection.cursor()

create_table = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(108) UNIQUE NOT NULL,
    age INT
    )
"""

insert_data = """
INSERT INTO users (username, email, age) VALUES
('jane', 'jane@doe.com', 20),
('bilal', 'bilal@gmail.com', 40),
('niah', 'gila@gmail.com', 67)
"""

cursor.execute(create_table)
cursor.execute(insert_data)

connection.commit()

select_data = "SELECT * FROM users"

cursor.execute(select_data)

users = cursor.fetchall()

for i in users:
    print(i)

cursor.close()
connection.close()

import sqlite3

# connect to database
conn = sqlite3.connect('student_records.db')

# create a cursor object for CRUD operations
cursor = conn.cursor()

# create table
table_info = """
create table student(name varchar(25), class varchar(25), section varchar(25))
"""

cursor.execute(table_info)

# insert some records
cursor.execute("""insert into student values('gaurav parajuli', 'machine learning', 'a')""")
cursor.execute("""insert into student values('animesh nepal', 'backend', 'b')""")
cursor.execute("""insert into student values('bishal pokharel', 'frontend', 'c')""")
cursor.execute("""insert into student values('anil magar', 'multimedia', 'd')""")
cursor.execute("""insert into student values('nabin khadka', 'frontend', 'c')""")
cursor.execute("""insert into student values('pawan dhakal', 'product management', 'e')""")
cursor.execute("""insert into student values('shanish dangol', 'project management', 'f')""")
cursor.execute("""insert into student values('sabba shah', 'ui/ux/content', 'g')""")
cursor.execute("""insert into student values('supriya maharjan', 'ui/ux/content', 'g')""")

print('data inserted are:')
data = cursor.execute('select * from student')
for row in data:
    print(row)
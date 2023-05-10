from faker import Faker
import mysql.connector
import uuid
import time

n = 10000
# create a new Faker instance
#fake = Faker()
#fake = Faker(['it_IT', 'en_US', 'ja_JP'])
fake = Faker(['ja_JP'])

# create a connection to the MySQL database
cnx = mysql.connector.connect(user='<user>', password='<password>',port=3306,
                              host='<Hostname>', database='<Schema>')
cursor = cnx.cursor()

# generate and insert fake data into the database
for i in range(n):
    uid = str(uuid.uuid4())
    cid = fake.random_number(digits=2)
    cfname = fake.first_name()
    clname = fake.last_name()
    description = fake.text()
    flag_id = fake.random_number(digits=1)
    created = fake.date()

    query = "INSERT INTO Dummy_Table (uuid,kind,via,item_id,payload,is_failed,created) VALUES (%s ,%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (uid, cid, cfname, clname, description, flag_id, created))
    cnx.commit()
    time.sleep(0.0001)
# close the database connection
cursor.close()
cnx.close()


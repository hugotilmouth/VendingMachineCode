# import the MySQLdb module
import MySQLdb

# establish a connection to the database
db = MySQLdb.connect(passwd="1234567891", db="ChargedUpDatabase", host="chargedupinstance.ch0v72mxdoau.eu-west-2.rds.amazonaws.com", port=3306, user="chargedUp")

# define your cursor
cursor = db.cursor()

# define and execute your MySQL query string
cursor.execute("SELECT * from Test")

# grab the rows in the query result and add to a variable
rows = cursor.fetchall()

# for each item in the rows variable, print item
for row in rows: print row

# release the database connection
db.close()


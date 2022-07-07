import pymysql

MYSQL_HOST = 'localhost'
MYSQL_CONN = pymysql.connect(
    host=MYSQL_HOST,
    port=3306,
    user='blog',
    passwd='blog1234',
    db='blog_db',
    charset='utf8'
)

SQL_cursor=MYSQL_CONN.cursor()
sql = 'SHOW TABLES;'
print(SQL_cursor.execute(sql))

sql = """
CREATE TABLE test (
    ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
    PRIMARY KEY(ID)
);
"""
SQL_cursor.execute(sql)
MYSQL_CONN.commit()

sql = 'DROP TABLE test;'
SQL_cursor.execute(sql)
MYSQL_CONN.commit()

user_email = 'test@test.com'
blog_id = 'id'

sql = "INSERT INTO user_info (USER_EMAIL, BLOG_ID) VALUES ('%s', '%s')" % (str(user_email), str(blog_id))
SQL_cursor.execute(sql)
MYSQL_CONN.commit()

sql = "SELECT * FROM user_info"
SQL_cursor.execute(sql)
results = SQL_cursor.fetchall()
for result in results:
    print (result, type(result))
    
user_id = 2
sql = "DELETE FROM user_info WHERE USER_ID = %d" % (user_id)
print(SQL_cursor.execute(sql))
MYSQL_CONN.commit()

MYSQL_CONN.close()
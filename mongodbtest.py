import pymongo

#mongodb연결
username = ''
password = ''
ip_address = 'localhost'
connection = pymongo.MongoClient()
connection = pymongo.MongoClient('mongodb://%s' % (ip_address))
test_session_db = connection.test_session_db
test = test_session_db.test

#연결확인
connection.admin.command('ismaster')
print(connection.server_info())

#데이터 삽입
test.insert_one({'id':'111'})
test.insert_one({'id':'222'})
test.insert_one({'id':'333'})

#데이터 조회
test.find_one({'id':'222'})

all_data=test.find()
for data in all_data:
    print(data)
    
#데이터 삭제
test.delete_one({'id':'222'})
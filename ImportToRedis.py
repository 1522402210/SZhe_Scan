import redis
# from index import app
from exts import db
from config import redisPool

'''
默认6379端口，第0个数据库
'''


def ToRedis():
    r = redis.Redis(connection_pool=redisPool)
    # r.flushdb()
    r.delete("SubScan")
    r.delete("SenScan")
    r.delete("XSSpayloads")
    r.delete("bugtype")
    file1 = open(r"dict/SUB_scan.txt", "r", encoding='utf-8')
    file2 = open(r"dict/SEN_scan.txt", "r", encoding='utf-8')
    file3=open('XSSBug/normal_payload.txt', 'r')
    file4=open('dict/bugtype.txt', 'r',encoding='utf-8')
    for line1 in file1.readlines():
        r.lpush("SubScan", line1.replace("\n", ''))
    file1.close()
    for line2 in file2.readlines():
        r.lpush("SenScan", line2.replace("\n", ""))
    file2.close()
    for line3 in file3.readlines():
        r.lpush("XSSpayloads",line3.replace("\n",""))
    file3.close()
    for line4 in file4.readlines():
        line4=line4.strip('\n')
        name=line4.split(":")[0]
        grade=line4.split(":")[1]
        r.hset('bugtype',name,grade)
    file4.close()

# def ToMySQL():
#     bugtype = open('dict/bugtype.txt', 'r')
#     with app.app_context():
#         for i in bugtype.readlines():
#             type,grade=i.split(":")[0],i.split(":")[1]
#             temp = BugType(bugtype=type,buggradeid=grade)
#             db.session.add(temp)
#         db.session.commit()
#     bugtype.close()
#     return None


ToRedis()
# ToMySQL()
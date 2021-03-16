import pymysql

db = pymysql.connect(host='####',user= '####',password= '####')
cursor = db.cursor()
print(cursor.execute("select version()"))
data = cursor.fetchone()
print(data)
# sql = '''create database label_detail'''
# cursor.execute(sql)
# cursor.connection.commit()
# cursor.
sql = '''use label_detail'''
cursor.execute(sql)
# sql = '''create table label_det (label_id varchar(200) not null, label_name varchar(200) not null, primary key (label_id))'''
# cursor.execute(sql)
sql = '''show tables'''
cursor.execute(sql)
print(cursor.fetchone())
# sql = '''insert into label_det (label_id, label_name) values ('%s','%s')''' % ('12whi-234-svs-356thb34', 'Regression')
# cursor.execute(sql)
# db.commit()
sql = '''select * from label_det'''
cursor.execute(sql)
values = cursor.fetchall()
db.commit()
print(type(values))
dic ={}
def Convert(tup,dic):
    for a,b in tup:
        dic.setdefault(a,b)
    return dic
print(Convert(values,dic))
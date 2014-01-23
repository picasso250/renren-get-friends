import MySQLdb

# try:
#     conn=MySQLdb.connect(host='localhost',user='root',passwd='',db='renren_data',port=3306)
#     cur=conn.cursor()
#     cur.execute('select * from test')
#     a = cur.fetchmany()
#     print a[0][0]
#     cur.close()
#     conn.close()
# except MySQLdb.Error,e:
#      print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def get_conn():
    try:
        return MySQLdb.connect(host='localhost',user='root',passwd='',db='renren_data',port=3306,charset="utf8")
    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def insert(form, row):
    try:
        conn=get_conn()
        cur=conn.cursor()
        sql = 'insert into '+form+' ('+','.join(row.keys())+') values ('+','.join(['%s' for x in row])+')'
        cur.execute(sql, row.values())
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def insert_on_duplicate(form, row):
    try:
        conn=get_conn()
        cur=conn.cursor()
        sql = 'insert into '+form+' ('+','.join(row.keys())+') values ('+','.join(['%s' for x in row])+') ON DUPLICATE KEY UPDATE '+','.join([x+'=%s' for x in row.keys()])
        print sql
        cur.execute(sql, row.values()+row.values())
        conn.commit()
        cur.close()
        conn.close()
    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])


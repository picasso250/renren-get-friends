import MySQLdb

try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='',db='renren_data',port=3306)
    cur=conn.cursor()
    cur.execute('select * from test')
    a = cur.fetchmany()
    print a[0][0]
    cur.close()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])

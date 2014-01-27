import MySQLdb

def find_one_val(sql, values=[]):
    row = find_one(sql, values)
    if row:
        return row[0]
    else:
        return None

def find_one(sql, values=[]):
    try:
        conn=get_conn()
        cur=conn.cursor()
        cur.execute(sql, values)
        row = cur.fetchone()
        cur.close()
        conn.close()
        if row:
            return row
        else:
            return None
    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def find_many_val(sql, values=[]):
    try:
        conn=get_conn()
        cur=conn.cursor()
        cur.execute(sql, values)
        ret = []
        while True:
            row = cur.fetchone()
            if row is None:
                break
            ret.append(row[0])
        cur.close()
        conn.close()
        return ret
    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def get_conn():
    try:
        return MySQLdb.connect(host='localhost',user='root',passwd='',db='santi',port=3306,charset="utf8")
    except MySQLdb.Error,e:
         print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def insert(form, row):
    try:
        conn=get_conn()
        cur=conn.cursor()
        sql = 'insert into '+form+' ('+','.join(row.keys())+') values ('+','.join(['%s' for x in row])+')'
        cur.execute(sql, row.values())
        insert_id = conn.insert_id()
        conn.commit()
        cur.close()
        conn.close()
        return insert_id
    except MySQLdb.Error,e:
        print sql
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def insert_on_duplicate(form, row):
    try:
        conn=get_conn()
        cur=conn.cursor()
        sql = 'insert into '+form+' ('+','.join(row.keys())+') values ('+','.join(['%s' for x in row])+') ON DUPLICATE KEY UPDATE '+','.join([x+'=%s' for x in row.keys()])
        cur.execute(sql, row.values()+row.values())
        insert_id = conn.insert_id()
        conn.commit()
        cur.close()
        conn.close()
        return insert_id
    except MySQLdb.Error,e:
        print sql
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

if __name__ == "__main__":
    images = find_many_val('select img from scene')

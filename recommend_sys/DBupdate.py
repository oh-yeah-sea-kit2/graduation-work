#coding:utf-8
import MySQLdb

def dbupdate(isbn10,isbn13,title,author,image_url,arasuji,tag):
        print
        #connect
        con = MySQLdb.connect(host='localhost',db="test",user="root",passwd="toor", charset="utf8")
        cur = con.cursor()
        title = title.encode('utf-8')
        #INSERT isbn10,isbn13,author,title,image_url,arasuji,con_tag
        cur.executemany("INSERT IGNORE INTO books(isbn10) VALUES (%s)",[(isbn10)])
        con.commit()
        """
        #UPDATE
        cur.execute('update books set isbn13 = %s,title = %s,author = %s,image_url = %s,arasuji = %s,tag = %s where isbn10 = %s',(isbn13,title,author,image_url,arasuji,tag,isbn10))
        con.commit()
        """
        #UPDATE title
        cur.execute('UPDATE books SET title = %s WHERE isbn10 = %s', (title,isbn10))
        con.commit()
        #UPDATE author
        cur.execute('UPDATE books SET author = %s WHERE isbn10 = %s',(author,isbn10))
        con.commit()
        #UPDATE image_url
        cur.execute('UPDATE books SET image_url = %s WHERE isbn10 = %s',(image_url,isbn10))
        con.commit()
        print 'isbn13' + isbn13
        #UPDATE isbn13
        cur.execute('UPDATE books SET isbn13 = %s WHERE isbn10 = %s',(isbn13,isbn10))
        con.commit()
        #UPDATE arasuji
        cur.execute('UPDATE books SET arasuji = %s WHERE isbn10 = %s',(arasuji,isbn10))
        con.commit()
        #print tag
        #UPDATE tag
        cur.execute('UPDATE books SET tag = %s WHERE isbn10 = %s',(tag,isbn10))
        con.commit()
        #Œã•Ð•t‚¯
        cur.close()
        con.close()
        return
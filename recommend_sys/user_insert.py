#coding:utf-8
import MySQLdb  #MySQLモジュールのインポート
from noun_tag import extractKeyword
from con_insert import con_insert
import charchk

def user_insert(uname,raw_documents):
        #文章を形態素解析し、名詞リストへ入れる
        #raw_documents は、文章データ
        noun_list = extractKeyword(raw_documents)
        #エンコードをチェックしてutf-8へ変換
        try:
                unicode(uname,"utf-8")
        except TypeError:
                uname = uname.encode('utf-8')
        else:
                uname_enc = charchk.g_enc(uname)
                uname = unicode(uname,uname_enc).encode('utf-8')
        #名詞リストをばらして文字列にする
        n = ','.join(noun_list)
        #DBへ接続をして、それぞれ格納
        con = MySQLdb.connect(host='localhost',db="test",user="root",passwd="toor", charset="utf8")
        cur = con.cursor()
        #INSERT ユーザー名
        cur.execute("INSERT INTO users(name,article,tag) VALUES (%s,%s,%s)",(uname,raw_documents,n))
        con.commit()#修正箇所（コミット）
        cur.execute('SELECT * FROM users where name = %s',(uname))
        res = cur.fetchall()
        #number
        for row in res:
                number = row[0]
        print 'user number:'
        print number
        #後片付け
        cur.close()
        con.close()
        con_insert(n)   #コンテンツの追加 n = 名詞タグの文字列
        return number
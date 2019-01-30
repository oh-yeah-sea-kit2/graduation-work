#coding:utf-8
import MySQLdb

def recommend(user_num):
        con_list = []
        #Connect
        con = MySQLdb.connect(host='localhost',db="test",user="root",passwd="toor", charset="utf8")
        cur = con.cursor()
        #SELECT
        cur.execute("SELECT * from percents where user_num = %s",(user_num))
        result = cur.fetchall()
        for row in result:
                pass
        #print row[4]
        try:
                row[4].split(',')
        except AttributeError:
                return 0
        #文字列をリスト型に変換
        reco_select = row[4].split(',')
        reco_list = []
        for row in reco_select:
                reco_list.append(row.split('-'))
        #print len(reco_list)
        for i in range(len(reco_list)):
                reco_num = reco_list[i][0]
                #レコメンドとして出力するコンテンツのデータを取り出す
                con_list.append(reco_con(reco_num))
        #リストの中にリストとして格納
        #print con_list
        #後片付け
        cur.close()
        con.close()
        #コンテンツのデータをリスト化したものを返す
        return con_list

def reco_con(reco_num):
        con_num = reco_num
        #Connect
        con = MySQLdb.connect(host='localhost',db="test",user="root",passwd="toor", charset="utf8")
        cur = con.cursor()
        #SELECT
        cur.execute("SELECT * from books where number = %s",(con_num))
        result = cur.fetchall()
        for row in result:
                pass
        data = {'title' : row[3],'author' : row[4],'image_url' : row[5],'arasuji' : row[6]}
        #'arasuji' : row[6]
        c_list = []
        #c_list.append(data)
        #print c_list
        return data
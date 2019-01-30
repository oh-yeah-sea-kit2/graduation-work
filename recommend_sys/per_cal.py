#coding:utf-8
import MySQLdb

#パーセントを計算してデータベースへ格納
def per_cal(con_num,user_num):
        connect = MySQLdb.connect(db='test',user='root',passwd='toor',charset='utf8')
        cur = connect.cursor()
        #コンテンツテーブルにタグがあるかどうか
        cur.execute('select * from books where number = %s',(con_num))
        result = cur.fetchall()
        for row in result:
                pass
        #コンテンツテーブルを表示
        #print row
        try:
                #コンテンツテーブルの８番目はタグ
                con_tag = row[7].split(',')
        except AttributeError:
                return 0
        else:
                pass
        con_tag = row[7].split(',')
        #
        user_num = user_num
        cur.execute('select * from users where number = %s',(user_num))
        result = cur.fetchall()
        for row in result:
                pass
        try:
                #ユーザテーブルの5番目はタグ
                user_tag = row[4].split(',')
        except AttributeError:
                return 0
        else:
                pass
        user_tag = row[4].split(',')
        #既に行ったものを省く
        cur.execute('select * from percents where user_num = %s',(user_num))
        result = cur.fetchall()
        for x in result:
                pass
        try:
                x == x
        except UnboundLocalError:
                pass
        else:
                if int(con_num) <= x[3]:
                        return 0
                else:
                        pass
        #set型
        c = set(con_tag)
        u = set(user_tag)
        #コンテンツとユーザの共通集合
        cu = c & u
        #print cu
        #ユーザタグに対するコンテンツタグのパーセント
        con_cnt = 0
        for i in cu:#いくつ同じか数える
                con_cnt += con_tag.count(i)

        per_c = 100.0 * (con_cnt)/len(con_tag)
        #print per_c ,'%'
        #コンテンツタグに対するユーザタグのパーセント
        user_cnt = 0
        for i in cu:#いくつ同じか数える
                user_cnt += user_tag.count(i)
        per_u = 100.0 * (user_cnt)/len(user_tag)
        #print per_u ,'%'
        #２数を足して割ったもの
        per = round((per_c + per_u)/2.0,2)
        #print per , '%'
        #insert か updateの判別
        cur.execute('select * from percents where user_num = %s',(user_num))
        res = cur.fetchall()
        for row2 in res:
                pass
        #数値を文字列に変換
        user_num = str(user_num)
        try:
                row2[1] == con_num
        except NameError:
                u_per = []
                con_num2 = str(con_num)
                per = str(per)
                u_per.append(con_num2 + '-'+ per)
                u_per = ','.join(u_per)
                cur.execute('insert into percents(user_num,percents,finished_num) values(%s,%s,%s)',(user_num,u_per,con_num))
                connect.commit()
                print 'insert OK !'
        else:
                #既に格納されているものを取り出して後ろに付け足
                #文字列をリストにして、perを新しくリストに追加　文字列>に直す
                u_per = row2[2].split(',')
                con_num2 = str(con_num)
                per = str(per)
                #print con_num2 + '-'+ per
                u_per.append(con_num2 + '-'+ per)
                #print u_per
                u_per = ','.join(u_per)

                cur.execute('update percents set percents = %s, finished_num = %s where user_num = %s',(u_per,con_num,user_num))
                connect.commit()
        # 後片付け
        cur.close()
        connect.close()
        return

#レコメンドとして出力するコンテンツを算出し、格納
def reco_cal(user_num):
        connect = MySQLdb.connect(db='test',user='root',passwd='toor',charset='utf8')
        cur = connect.cursor()
        cur.execute('select * from percents where user_num = %s',(user_num))
        result = cur.fetchall()
        for row in result:
                pass
        #パーセントテーブルのコンテンツナンバーとパーセントを分ける
        i = row[2].split(',')
        #print len(i)
        #listの初期化
        per_list = []
        for row in i:
                per_list.append(row.split('-'))
        reco_list = []
        per_threshold = 20      #20%以上をレコメンド
        for row in per_list:#閾値を元にふるいに掛ける
                if  20 <= float(row[1]):
                        reco_list.append(row)
                else:
                        pass
        #print reco_list
        #レコメンド結果として出力するコンテンツリストから文字列へ
        reco_list2 = []
        for row in reco_list:
                reco_list2.append('-'.join(row))
        reco_list3 = ','.join(reco_list2)
        cur.execute('update percents set recommend = %s where user_num = %s',(reco_list3,user_num))
        connect.commit()
        #後片付け
        cur.close()
        connect.close()
        return

#メイン処理
def per_cal_main(user_num):
        connect = MySQLdb.connect(db='test',user='root',passwd='toor',charset='utf8')
        cur = connect.cursor()
        #コンテンツ数を数えてそれぞれ処理
        cur.execute('select * from books')
        res = cur.fetchall()
        i = 1
        cnt = len(res) + 1
        while True:
                if i >= cnt:
                        break
                #print i, '番目:'
                cur.execute('select * from books where number = %s',(i))
                res2 = cur.fetchall()
                if res2 == ():
                        i += 1
                        cnt += 1
                        #リストは空
                else:
                        per_cal(i,user_num)
                        i += 1
        #すべての計算が終わったあとレコメンドとして算出するものを出す
        reco_cal(user_num)
        # 後片付け
        cur.close()
        connect.close()
        return
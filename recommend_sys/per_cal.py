#coding:utf-8
import MySQLdb

#�p�[�Z���g���v�Z���ăf�[�^�x�[�X�֊i�[
def per_cal(con_num,user_num):
        connect = MySQLdb.connect(db='test',user='root',passwd='toor',charset='utf8')
        cur = connect.cursor()
        #�R���e���c�e�[�u���Ƀ^�O�����邩�ǂ���
        cur.execute('select * from books where number = %s',(con_num))
        result = cur.fetchall()
        for row in result:
                pass
        #�R���e���c�e�[�u����\��
        #print row
        try:
                #�R���e���c�e�[�u���̂W�Ԗڂ̓^�O
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
                #���[�U�e�[�u����5�Ԗڂ̓^�O
                user_tag = row[4].split(',')
        except AttributeError:
                return 0
        else:
                pass
        user_tag = row[4].split(',')
        #���ɍs�������̂��Ȃ�
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
        #set�^
        c = set(con_tag)
        u = set(user_tag)
        #�R���e���c�ƃ��[�U�̋��ʏW��
        cu = c & u
        #print cu
        #���[�U�^�O�ɑ΂���R���e���c�^�O�̃p�[�Z���g
        con_cnt = 0
        for i in cu:#����������������
                con_cnt += con_tag.count(i)

        per_c = 100.0 * (con_cnt)/len(con_tag)
        #print per_c ,'%'
        #�R���e���c�^�O�ɑ΂��郆�[�U�^�O�̃p�[�Z���g
        user_cnt = 0
        for i in cu:#����������������
                user_cnt += user_tag.count(i)
        per_u = 100.0 * (user_cnt)/len(user_tag)
        #print per_u ,'%'
        #�Q���𑫂��Ċ���������
        per = round((per_c + per_u)/2.0,2)
        #print per , '%'
        #insert �� update�̔���
        cur.execute('select * from percents where user_num = %s',(user_num))
        res = cur.fetchall()
        for row2 in res:
                pass
        #���l�𕶎���ɕϊ�
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
                #���Ɋi�[����Ă�����̂����o���Č��ɕt����
                #����������X�g�ɂ��āAper��V�������X�g�ɒǉ��@������>�ɒ���
                u_per = row2[2].split(',')
                con_num2 = str(con_num)
                per = str(per)
                #print con_num2 + '-'+ per
                u_per.append(con_num2 + '-'+ per)
                #print u_per
                u_per = ','.join(u_per)

                cur.execute('update percents set percents = %s, finished_num = %s where user_num = %s',(u_per,con_num,user_num))
                connect.commit()
        # ��Еt��
        cur.close()
        connect.close()
        return

#���R�����h�Ƃ��ďo�͂���R���e���c���Z�o���A�i�[
def reco_cal(user_num):
        connect = MySQLdb.connect(db='test',user='root',passwd='toor',charset='utf8')
        cur = connect.cursor()
        cur.execute('select * from percents where user_num = %s',(user_num))
        result = cur.fetchall()
        for row in result:
                pass
        #�p�[�Z���g�e�[�u���̃R���e���c�i���o�[�ƃp�[�Z���g�𕪂���
        i = row[2].split(',')
        #print len(i)
        #list�̏�����
        per_list = []
        for row in i:
                per_list.append(row.split('-'))
        reco_list = []
        per_threshold = 20      #20%�ȏ�����R�����h
        for row in per_list:#臒l�����ɂӂ邢�Ɋ|����
                if  20 <= float(row[1]):
                        reco_list.append(row)
                else:
                        pass
        #print reco_list
        #���R�����h���ʂƂ��ďo�͂���R���e���c���X�g���當�����
        reco_list2 = []
        for row in reco_list:
                reco_list2.append('-'.join(row))
        reco_list3 = ','.join(reco_list2)
        cur.execute('update percents set recommend = %s where user_num = %s',(reco_list3,user_num))
        connect.commit()
        #��Еt��
        cur.close()
        connect.close()
        return

#���C������
def per_cal_main(user_num):
        connect = MySQLdb.connect(db='test',user='root',passwd='toor',charset='utf8')
        cur = connect.cursor()
        #�R���e���c���𐔂��Ă��ꂼ�ꏈ��
        cur.execute('select * from books')
        res = cur.fetchall()
        i = 1
        cnt = len(res) + 1
        while True:
                if i >= cnt:
                        break
                #print i, '�Ԗ�:'
                cur.execute('select * from books where number = %s',(i))
                res2 = cur.fetchall()
                if res2 == ():
                        i += 1
                        cnt += 1
                        #���X�g�͋�
                else:
                        per_cal(i,user_num)
                        i += 1
        #���ׂĂ̌v�Z���I��������ƃ��R�����h�Ƃ��ĎZ�o������̂��o��
        reco_cal(user_num)
        # ��Еt��
        cur.close()
        connect.close()
        return
#coding:utf-8
import MySQLdb  #MySQL���W���[���̃C���|�[�g
from noun_tag import extractKeyword
from con_insert import con_insert
import charchk

def user_insert(uname,raw_documents):
        #���͂��`�ԑf��͂��A�������X�g�֓����
        #raw_documents �́A���̓f�[�^
        noun_list = extractKeyword(raw_documents)
        #�G���R�[�h���`�F�b�N����utf-8�֕ϊ�
        try:
                unicode(uname,"utf-8")
        except TypeError:
                uname = uname.encode('utf-8')
        else:
                uname_enc = charchk.g_enc(uname)
                uname = unicode(uname,uname_enc).encode('utf-8')
        #�������X�g���΂炵�ĕ�����ɂ���
        n = ','.join(noun_list)
        #DB�֐ڑ������āA���ꂼ��i�[
        con = MySQLdb.connect(host='localhost',db="test",user="root",passwd="toor", charset="utf8")
        cur = con.cursor()
        #INSERT ���[�U�[��
        cur.execute("INSERT INTO users(name,article,tag) VALUES (%s,%s,%s)",(uname,raw_documents,n))
        con.commit()#�C���ӏ��i�R�~�b�g�j
        cur.execute('SELECT * FROM users where name = %s',(uname))
        res = cur.fetchall()
        #number
        for row in res:
                number = row[0]
        print 'user number:'
        print number
        #��Еt��
        cur.close()
        con.close()
        con_insert(n)   #�R���e���c�̒ǉ� n = �����^�O�̕�����
        return number
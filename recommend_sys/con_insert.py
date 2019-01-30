#coding:utf-8
import MySQLdb
from charchk import g_enc
from amazon import Amazon
from HTMLParser import HTMLParser
from noun_tag import extractKeyword
from htmlentity2utf8 import htmlentity2utf8
from DBupdate import dbupdate

#���[�U�[�^�O�����ɃR���e���c��ǉ����Ă���
def con_insert(noun):   #noun�̓^�O�̏W��(tags)
        #����������X�g�ɕϊ�
        noun_tag = noun.split(",")
        con_isbn_list = []
        for noun in noun_tag:
                #Unicode�ȊO��ϊ�
                noun = noun.decode(g_enc(noun))
                con_search(noun)
        return

def con_search(keyword):
        amazon = Amazon("", "")
        xml = amazon.itemSearch("Books", Keywords = keyword, ItemPage="1")
        
        # XML����������o��
        from BeautifulSoup import BeautifulStoneSoup
        soup = BeautifulStoneSoup(xml)
        #10�̃R���e���c���R���e���c�e�[�u���֊i�[
        for item in soup.findAll('item'):
                isbn10 = item.asin.contents[0]
                #issbn13
                #isbn13 = item.ean.contents[0]
                isbn13 = ''
                #author
                try:	#author�i���ҁj�͂Ȃ��ꍇ������̂ŃG���[����
                        author = item.author.contents[0]
                except AttributeError:
                        author = ""
                else:
                        author = item.author.contents[0]
                title = item.title.contents[0]
                #url
                url = item.detailpageurl.contents[0]
                #image_url
                try:
                        image_url = item.largeimage.url.contents[0]
                except NameError:
                        image_url = ""
                except AttributeError:
                        image_url = ""
                else:
                        image_url = item.largeimage.url.contents[0]
                arasuji = HTMLParser(url)
                #�����Q�Ƃ�ϊ�����
                arasuji = htmlentity2utf8(arasuji)
                #���炷�����炢��Ȃ������A�L������菜��
                #print arasuji
                con_tag = extractKeyword(arasuji)
                con_tag = ','.join(con_tag)
                #print title,isbn10
                #DB�֊i�[����
                dbupdate(isbn10,isbn13,title,author,image_url,arasuji,con_tag)
        return
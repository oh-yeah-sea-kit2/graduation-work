#coding:utf-8
import MySQLdb
from charchk import g_enc
from amazon import Amazon
from HTMLParser import HTMLParser
from noun_tag import extractKeyword
from htmlentity2utf8 import htmlentity2utf8
from DBupdate import dbupdate

#ユーザータグを元にコンテンツを追加していく
def con_insert(noun):   #nounはタグの集合(tags)
        #文字列をリストに変換
        noun_tag = noun.split(",")
        con_isbn_list = []
        for noun in noun_tag:
                #Unicode以外を変換
                noun = noun.decode(g_enc(noun))
                con_search(noun)
        return

def con_search(keyword):
        amazon = Amazon("", "")
        xml = amazon.itemSearch("Books", Keywords = keyword, ItemPage="1")
        
        # XMLから情報を取り出す
        from BeautifulSoup import BeautifulStoneSoup
        soup = BeautifulStoneSoup(xml)
        #10個のコンテンツをコンテンツテーブルへ格納
        for item in soup.findAll('item'):
                isbn10 = item.asin.contents[0]
                #issbn13
                #isbn13 = item.ean.contents[0]
                isbn13 = ''
                #author
                try:	#author（著者）はない場合があるのでエラー処理
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
                #文字参照を変換する
                arasuji = htmlentity2utf8(arasuji)
                #あらすじからいらない文字、記号を取り除く
                #print arasuji
                con_tag = extractKeyword(arasuji)
                con_tag = ','.join(con_tag)
                #print title,isbn10
                #DBへ格納する
                dbupdate(isbn10,isbn13,title,author,image_url,arasuji,con_tag)
        return
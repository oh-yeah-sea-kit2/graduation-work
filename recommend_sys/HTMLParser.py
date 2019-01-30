#coding:utf-8
from BeautifulSoup import BeautifulSoup
import urllib2
import re

def HTMLParser(url):
        # Web からデータを取得する
        html = urllib2.urlopen(url).read()
        soup = BeautifulSoup(html)

        records = []
        # class 属性が mtx である tr タグを対象に
        for div in soup('div', {'class':'productDescriptionWrapper'}):
            rec = []
            data = div.renderContents().strip()
            rec.append(data)
            if rec != []: records.append(rec)

        # 取得したデータを出力する
        a=[]
        for rec in records:
            for i, data in enumerate(rec):
                #print unicode(data, 'utf-8'), "\t",
                a.append(data)

        data =  a[0]
        data2 = data
        #不要な文字列の削除
        r1 = re.compile('<div class="emptyClear"> </div>')
        r2 = re.compile('<br />')
        r3 = re.compile('< b >')
        r4 = re.compile('</ b >')
        r5 = re.compile('&lt;')
        r6 = re.compile('&gt;')
        data = re.sub(r1, '',data)
        data = re.sub(r2, '',data)
        data = re.sub(r3, '',data)
        data = re.sub(r4, '',data)
        data = re.sub(r5, '',data)
        data = re.sub(r6, '',data)
        return data
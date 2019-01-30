#coding:utf-8
import MeCab
from charchk import g_enc

def extractKeyword(text):
        u"""textを形態素解析して、名詞のみのリストを返す"""
        #文字コード判別
        print g_enc(text)
        #textをutf-8へ変換
        if g_enc(text) == "unicode":
                text_enc = text.encode('utf-8')
        elif g_enc(text) == "utf-8":
                text_enc = text
        else:
                text_enc = text
        tagger = MeCab.Tagger()
        #print text
        """
        encoded_text = []
        for d in text:
        """
        encoded_text = text_enc
        node = tagger.parseToNode(encoded_text).next
        keywords = []
        while node:
                if node.feature.split(",")[0] == "名詞":
                        keywords.append(node.surface)
                node = node.next
        """
        for i in keywords:
                #print i
                pass
        """
        return keywords
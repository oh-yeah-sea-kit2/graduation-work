#coding:utf-8

def g_enc(s):
        encodings = ["ascii","utf-8","shift-jis","enc-jp"]
        for enc in encodings:
                try:
                        unicode(s,enc)
                        break
                except UnicodeDecodeError,e:
                        enc = ""
                except TypeError,e:
                        enc = "unicode"
        return enc
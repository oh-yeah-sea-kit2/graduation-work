#!-*- coding:utf-8 -*-
import htmlentitydefs
import re

# ���̎Q�� & �����Q�Ƃ�ʏ�̕����ɖ߂�
def htmlentity2utf8(text):
    # ���K�\���̃R���p�C��
    reference_regex = re.compile(u'&(#x?[0-9a-f]+|[a-z]+);', re.IGNORECASE)
    num16_regex = re.compile(u'#x\d+', re.IGNORECASE)
    num10_regex = re.compile(u'#\d+', re.IGNORECASE)

    text = unicode(text,'utf-8')
    result = u''
    i = 0
    while True:
        # ���̎Q�� or �����Q�Ƃ�������
        match = reference_regex.search(text, i)
        if match is None:
            try:
                result += text[i:]
            except UnicodeDecodeError:
                return text
            else:
                result += text[i:]
            break

        result += text[i:match.start()]
        i = match.end()
        name = match.group(1)

        # ���̎Q��
        if name in htmlentitydefs.name2codepoint.keys():
            result += unichr(htmlentitydefs.name2codepoint[name])
        # �����Q��
        elif num16_regex.match(name):
            # 16�i��
            result += unichr(int(u'0'+name[1:], 16))
        elif num10_regex.match(name):
            # 10�i��
            result += unichr(int(name[1:]))
    result = result.encode('utf-8')
    return result
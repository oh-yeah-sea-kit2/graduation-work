#coding:utf-8
import shelve
from datetime import datetime
import xml.sax.saxutils

from flask import Flask,request,render_template,redirect,escape,Markup
from recommend import recommend
from user_insert import user_insert
from per_cal import per_cal_main

application = Flask(__name__)
user_num = 1

def save_data(name,comment,create_at):
        uname = name
        raw_documents = comment
        print create_at
        global user_num
        #user_num = 15
        user_num = user_insert(uname,raw_documents)
        print "user_num INSERT"
        per_cal_main(user_num)
        #greeting_list = recommend(user_num)
        return user_num

def load_data():
        global user_num
        print user_num
        greeting_list = recommend(user_num)
        return greeting_list

@application.route('/')
def index():
        greeting_list = load_data()
        return render_template('index.html',greeting_list=greeting_list)

@application.route('/post',methods=['post'])
def post():
        name = request.form.get('name')
        comment = request.form.get('comment')
        create_at = datetime.now()
        save_data(name,comment,create_at)
        #user_num = save_at(name, comment,create_at)
        return redirect('/')

@application.template_filter('unescape')
def unescape_filter(s):
        return xml.sax.saxutils.unescape(s)

@application.template_filter('datetime_fmt')
def datetime_fmt_filter(dt):
        return dt.strftime('%Y/%m/%d %H:%M:%S')

if __name__ == '__main__':
        application.run('192.168.0.3',debug=True)
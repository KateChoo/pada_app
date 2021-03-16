import os
import time
import datetime
#from flask_wtf import FlaskForm
from flask import Flask, render_template, request, session, redirect, url_for, flash, jsonify

app = Flask(__name__)
app.config['SECRET_KEY'] = "pada_app"

author_name = "K"
web_info = {
    'dir_t': '歡迎光臨，目錄',
    'signin_t': '歡迎光臨，請輸入帳號密碼',
    'upload_t': 'Upload, maybe',
    'taipei_t': '歡迎光臨，台北',
    'member_t': '歡迎光臨，這是會員頁面',
    'error_t': '失敗頁面',
}
# print(app.config)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
titles = ['pada_0']

# while True:
#     t = 0
#     titles.append['pada_' + str(t)]
#     t += 1
#     if t < 2:
#         break
show_link = False


class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'[User]: {self.username}'


users = []
users.append(User(id=1, username='test', password='test'))
print(users)


@app.route('/', methods=['GET', 'POST'])
def home():
    print('logining')

    return render_template('/pada_3.html',
                           web_info=web_info,
                           )


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if (username == 'test') and (password == 'test'):
        return redirect('/member/')
    else:
        return redirect('/error/')


@app.route('/member/', methods=['GET', 'POST'])
def member():
    return render_template('member.html',
                           web_info=web_info
                           )


@app.route('/error/')
def error():
    return render_template('error.html',
                           web_info=web_info
                           )


@ app.route('/pada_2')
def pada_2():
    return render_template('/pada_2.html',
                           web_info=web_info,
                           )


@app.route('/dir')
def dir():
    return render_template('index.html',
                           web_info=web_info,  # ??
                           title=titles[0],
                           author_name=author_name,
                           show_link=show_link
                           )


app.config['IMAGE_UPLOADS'] = '/Users/choochoo/Desktop/2021/pongpong/pada_app/static/img/uploads'


@app.route('/pada_1', methods=['GET', 'POST'])
def pada_1():
    if request.method == 'GET':
        if request.files:
            image = request.files['image']

            # .save, method on the filestorage
            image.save(os.path.join(
                app.config['IMAGE_UPLOADS'], image.filename))

            print('Image Saved')
            return redirect(request.url)
            # pass
    return render_template('/pada_1.html',
                           web_info=web_info
                           )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
# if __name__ == '__main__':
#     port = int(os.environ.get("PORT", 5000))
#     app.run(debug=True, port=port, host="0.0.0.0")

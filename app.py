from flask import Flask, render_template
app = Flask(__name__)

author_name = "K"
# print(app.config)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# web_info = {
#     "title": "~~",
#     "subtitle": "Welcome",

# }
titles = ['pada_0']

# while True:
#     t = 0
#     titles.append['pada_' + str(t)]
#     t += 1
#     if t < 2:
#         break
show_link = False


@app.route('/')
def home():
    return render_template('index.html',
                           title=titles[0],
                           author_name=author_name,
                           show_link=show_link
                           )


@ app.route('/pada_0')
def pada_0():
    return render_template('/pada_0.html')


if __name__ == '__main__':
    app.run(debug=True, port=5500)

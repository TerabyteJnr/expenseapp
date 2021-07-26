from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(host="remotemysql.com", user="hmbIEv0Yo6", password="AQFfhdveF5",
                               database="sql11426049", )
cursor = conn.cursor()


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/register')
def about():
    return render_template('register.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/login_validation', methods=['POST'])
def login_validation():
    email = request.form.get('email')
    password = request.form.get('password')

    cursor.excute("""SELECT * FROM `Users` WHERE `email` LIKE '{}' AND `password` LIKE '{}'"""
                  .format(email, password))
    Users = cursor.fetchall()
    if len(Users) > 0:
        return render_template('home.html')
    else:
        return render_template('login.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    name=request.form.get('uname')
    email=request.form.get('uemail')
    password=request.form.get('upassword')

    cursor.execute("""INSERT INTO `Users`(`user_id`,`name`,`email`,`password`)
    VALUES (NULL, '{}','{}','{}')""".format(name,email,password))
    conn.commit()
    return "..."


if __name__ == "__main__":
    app.run(debug=True)

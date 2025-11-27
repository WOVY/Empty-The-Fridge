from flask import Flask, render_template, request, redirect, url_for, session, flash
import database as db
import config

app = Flask(__name__)
app.config.from_object(config)

@app.route('/')
def index():
        return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        password = request.form.get('password')
        nickname = request.form.get('nickname')
        if db.register_user(user_id, password, nickname):
            flash('회원가입 성공! 로그인해주세요.', 'success')
            return redirect(url_for('login'))
        else:
            flash('회원가입 실패. 이미 존재하는 아이디입니다.', 'error')
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)
    
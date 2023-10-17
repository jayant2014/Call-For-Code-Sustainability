from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)

# Mock user data (you should use a database)
users = {
    'user1': {'password': 'password1'},
    'user2': {'password': 'password2'}
}

class User(UserMixin):
    pass

@login_manager.user_loader
def load_user(username):
    if username in users:
        user = User()
        user.id = username
        return user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            user = User()
            user.id = username
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Login failed. Please check your credentials.', 'danger')
    return render_template('login.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', username=current_user.id)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)

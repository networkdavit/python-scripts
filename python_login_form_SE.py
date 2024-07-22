from flask import Flask, request, render_template_string

app = Flask(__name__)

# I am writing here a temporary HTML form, you should change it to whatevre you please, and also you can add css
login_form = """
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
</head>
<body>
    <h2>Login Form</h2>
    <form method="post" action="/login">
        <div>
            <label for="username">Username:</label>
            <input type="text" id="username" name="username">
        </div>
        <div>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password">
        </div>
        <div>
            <button type="submit">Login</button>
        </div>
    </form>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(login_form)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    print(f"Username: {username}")
    print(f"Password: {password}")
    return "some redirect should happen here"

if __name__ == '__main__':
    app.run(debug=True)

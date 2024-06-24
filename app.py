from flask import Flask, render_template

app = Flask(__name__)

# Routes
@app.route('/')
def LoginAndSignup():
    return render_template('LoginAndSignup.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/more')
def more():
    return render_template('more.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

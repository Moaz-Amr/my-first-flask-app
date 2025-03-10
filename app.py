from flask import Flask, render_template

print(__name__)

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1 style = "color:green;">Hello world !</h1>'
    # return render_template('hello.html')

@app.route('/about/')
def about():
    return '<h1 style = "color:red;">Hello from about !</h1>'

#<h1 style = "color:green">hello world </h1>
if __name__ == '__main__':#يعتبر documentation
    app.run(debug=True, port=3000)#run the app
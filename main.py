from flask import Flask, render_template, url_for, flash, session, request, redirect

app = Flask(__name__)
app.secret_key = 'lamePass1234'

@app.route("/")
def index():
    return render_template("index.html")
    


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template,request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello_world():

    return render_template('index.html')

@app.errorhandler(400)      #to handel the 400(bad request error)
def page_not_found(e):
    return render_template('index.html')

if __name__ == "__main__":

    # lets launch our webpage!
    # do 0.0.0.0 so that we can log into this webpage
    # using another computer on the same network later
    app.run(host='0.0.0.0')

from flask import Flask, render_template
app=Flask(__name__)

@app.route('/if')
def hello_if():
    value=27
    return render_template('condition.html',data=value)

if __name__=='__main__':
    app.run(host='127.0.0.1',port='8080')
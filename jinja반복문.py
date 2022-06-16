from flask import Flask, render_template
app=Flask(__name__)

@app.route('/loop')
def loop():
    value_list=['반','복','문',1,3,7]
    return render_template('loop.html',values=value_list)

if __name__=='__main__':
    app.run(host='127.0.0.1',port='8080')
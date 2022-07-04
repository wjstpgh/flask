# dave_server.py
from flask import Flask
from sub_blueprint import sub_bp

app = Flask(__name__)
app.register_blueprint(sub_bp.bp, url_prefix='/ccc')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='8080')

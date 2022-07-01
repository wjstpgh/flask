from flask import Flask

app = Flask(__name__)

#결로를 찾지 못했을 때, Not Found
@app.errorhandler(404)
def page_not_found(error):
    return "<h1>404 Error 발생!</h1>", 404

#제대로 경로를 찾았을 때, code 200
@app.route("/home")
def home_page():
    return '경로에 있는 페이지'

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080")

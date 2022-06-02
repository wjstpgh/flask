#request는 url뒤의 파라미터값을 넣기위함
from flask import Flask,jsonify,request,render_template

#객체생성
app=Flask(__name__)

#로그인페이지 구현
@app.route('/login')
def login():
    #get방식으로 파라미터값 받기
    username=request.args.get('user_name')
    pw=request.args.get('pass_word')
    print(username,pw)
    #id가 newyork일때만 인증성공
    if username=='newyork':
        return_data={'auth':'success'}
    else:
        return_data={'auth':'failed'}
    return jsonify(return_data)

@app.route('/html_test')
def hello_html():
    #templates폴더의 로그인폼 렌더링
    return render_template('login.html')

if __name__=='__main__':
    app.run(host='127.0.0.1',port='8080')


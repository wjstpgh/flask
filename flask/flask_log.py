from flask import Flask

app = Flask(__name__)

if not app.debug:
    import logging
    # FileHandler - 파일로 로그를 저장
    # RotatingFileHandler - 파일이 일정 사이즈를 넘어가면 새 파일을 생성해서 저장
    # NTEventLogHandler - 윈도우 시스템 로그로 남김
    # SysLogHandler - 유닉스 계열 시스템의 syslog 로 남김
    from logging.handlers import RotatingFileHandler
    # maxBytes=하나의파일사이즈, backupCount=파일갯수
    # 전체 파일을 다 쓰면, 다시 처음부터 씀
    file_handler = RotatingFileHandler(
        'flask_log.log', maxBytes=2000, backupCount=10)
    file_handler.setLevel(logging.WARNING)
    # app.logger.addHandler() 에 등록시켜줘야 app.logger 로 사용 가능
    app.logger.addHandler(file_handler)

@app.errorhandler(404)
def page_not_found(error):
    import datetime as date
    d=date.datetime.now()
    app.logger.error('where:page_not_found;when:{0}.{1}.{2};port:8080'.format(d.year,d.month,d.day))
    return "<h1>해당 페이지를 찾을수가 없어요ㅠㅠ</h1>", 404

if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080", debug=False)

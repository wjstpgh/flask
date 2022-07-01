import logging
# filename='로그를 저장할 파일' level=로그로 남길 에러 단계 지정
logging.basicConfig(filename='test.log', level=logging.ERROR)

# 로그를 남길 부분에 다음과 같이 로그 레벨에 맞추어 출력해주면 해당 내용이 파일에 들어감
logging.debug("debug 311")
logging.info("info 323")
logging.warning("warning 111")
logging.error("error 024")
logging.critical("critical 444")
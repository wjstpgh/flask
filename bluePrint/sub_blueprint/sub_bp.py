# blog_test.py
from flask import Blueprint

bp = Blueprint('sub', __name__)

# http://localhost:8080/ccc/bbb 
@bp.route('/bbb')
def blog():
    return 'TEST BLUEPRINT'

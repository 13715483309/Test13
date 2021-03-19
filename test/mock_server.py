import sys
sys.path.append('/Users/chenjinfei/project/pythonProject/test')

from flask import Flask,Response,jsonify,json,request
from throught import passThought

app = Flask(__name__)

@app.route('/login',methods=['POST'])
def login():
    url = 'login'
    data = json.loads(request.get_data(as_text=True))
    name = data['name']
    if name == '被锁定':
        return jsonify({'code':402,'name':'被锁定','res':'用户被锁定'})
    elif name == '黑名单':
        return jsonify({'code':403,'name':'被锁定','res':'黑名单'})
    else:
        resp = passThought(url,data)
        return resp

@app.route('/<func>',methods=['POST'])
def throught(func):
    data = json.loads(request.get_data(as_text=True))
    resp = passThought(url=func,data=data)
    return resp

if __name__ == '__main__':
    app.run(port=5001)
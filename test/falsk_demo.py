# flask框架
from flask import Flask,Response,json,request,jsonify
import csv

app = Flask(__name__)

@app.route('/register',methods=["POST"])
def register():
    data = json.loads(request.get_data(as_text = True))
    name = data['name']
    pwd = data['pwd']
    try:
        # reg_write_csv(name,pwd)
        path = 'data.csv'
        with open(path, 'a+', encoding='utf-8') as f:
            reg_write_csv = csv.writer(f)
            data_row = [name, pwd]
            reg_write_csv.writerow(data_row)
        data = {'name':name, 'message':'注册成功','code':200}
        return jsonify(data)
    except Exception as e:
        print(f'发生异常，原因是{e}')
        data = {'name':name,'message':e,'code':201}
        return jsonify(data)

@app.route('/login',methods=['POST'])
def login():
    data = json.loads(request.get_data(as_text=True))
    name = data['name']
    pwd = data['pwd']
    path = 'data.csv'
    with open(path, encoding='utf-8') as f:
        read = csv.reader(f)
        for row in read:
            if name in row and pwd in row:
                return {'name':name, 'message':'登录成功','code':200}
        return {'name':name,'message':'失败','code':201}

if __name__ == '__main__':
    app.run(port=5000)
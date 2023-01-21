from flask import Flask,request

app = Flask(__name__)

@app.route('/api',methods = ['GET'])
def myfunc():
    d = str(request.args['query'])
    illness = d['illness']
    remedies = d['remedies']

    return d

if __name__ == '__main__':
    app.run()
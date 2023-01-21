from flask import Flask,request
from get_url import get_url
from tester import brain

app = Flask(__name__)

@app.route('/api',methods = ['GET'])
def myfunc():
    d = str(request.args['query'])
    d = d[1:-1]
    d = d.split(', ')
    print(d)
    illness = d[0]
    remedies = d[1:]
    content,sites = get_url(illness,remedies)
    print(content)
    ans = brain(content)
    d = dict()
    ans = list(map(lambda x: 2*x-1,ans))
    d['ans'] = ans
    d['sites'] = sites
    return d

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4040)

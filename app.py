import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('http://20.231.9.117:80')
    if response.status_code == 200:
        data = response.json()
        print(data)
        return 'Success'
    else:
        return 'Error'

if __name__ == '__main__':
    app.run()

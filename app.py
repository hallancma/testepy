from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Service Python rodando na porta 5000 no Coolify!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

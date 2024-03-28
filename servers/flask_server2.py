from flask import Flask
PORT_NUMBER = 3001

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hi from Flask Server 2'

if __name__ == '__main__':
	app.run(port=PORT_NUMBER)

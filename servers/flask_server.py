from flask import Flask
PORT_NUMBER = 3000

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hi from Flask Server 1'

if __name__ == '__main__':
	app.run(port=PORT_NUMBER)

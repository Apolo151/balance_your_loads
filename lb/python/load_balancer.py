from flask import Flask
PORT_NUMBER = 8000

app = Flask(__name__)

@app.route('/')
def Hi():
	return 'Hi from load balancer'

if __name__ == '__main__':
	app.run(port=PORT_NUMBER)

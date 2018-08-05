from flask import Flask, send_from_directory
from flask_socketio import SocketIO, send

app = Flask(__name__, static_url_path='')

app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

@socketio.on('message')
def handleMessage(msg):
    print('Message: '+ msg)

    # This line sends the message received to all 
    # the other clients that are connected.
    #send(msg, broadcast=True)

@socketio.on("Brandon")
def Brandon_event(number):
    print("The number is: ", number)

@socketio.on('connection')
def ConnectionEvent(val):
    print("There is a client connected "+val)

@app.route("/")
def index():
   return send_from_directory('./','index.html')

if __name__ == '__main__':
    print("The server is running")
    print("the server is listening")
    socketio.run(app)
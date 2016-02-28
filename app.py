from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)



# Server side
@socketio.on('connect')
def on_connect():
    print 'client connected!'
    
    string = {"data":
                [{"clients":
                        [{"client0":
                            [{"tl": [0,500] },
                            {"tr": [100,500] },
                            {"bl": [0,0] },
                            {"br": [100,0] }]
                        },
                        {"client1":
                            [{"tl": [200,500] },
                            {"tr": [300,500] },
                            {"bl": [200,0] },
                            {"br": [300,0] }]
                        }]
                },
                {"balls":
                    [
                        {"globalPosition": [10,10]},
                        {"position": [10,10]},
                    ]
                }]
            }
            
    emit('position', string)

if __name__ == '__main__':
    socketio.run(app)

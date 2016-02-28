from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
import json
import time
from __future__ import print_function

import ftd2xx as FT
import numpy as np
import matplotlib.pyplot as plt
import time
from scipy import stats
import cluster

import sys 



app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


string = {"data":
                    [{"clients":
                            [{"client0":
                                [{"tl": [6,23] },
                                {"tr": [16,5] },
                                {"bl": [18,29] },
                                {"br": [26,11] }]
                            },
                            {"client1":
                                [{"tl": [27,7] },
                                {"tr": [41,31] },
                                {"bl": [47,4] },
                                {"br": [54,29] }]
                            }]
                    },
                    {"balls":
                        [
                            {'phone': 0},
                            {"globalPosition": [16,18]},
                            {"position": [10,10]},
                            {"velocity": [3,3]}
                        ]
                    }]
                }    

# Server side

@socketio.on('connect')
def on_connect():
    print "connected!"
    emit('position', string)

@socketio.on('more')
def more(more):
    emit('position', string)
    

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=80 )


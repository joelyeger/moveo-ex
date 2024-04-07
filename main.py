import os

from website import create_app

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = create_app()
socketio = SocketIO(app)

connected_clients = {"amount": 0}


@socketio.on('connect')
def handle_connect():

    connected_clients["amount"] += 1
    if connected_clients["amount"] == 1:
        emit('mode', {'mode': 'read_only'})
    else:
        emit('mode', {'mode': 'read_write'})


@socketio.on('disconnect')
def handle_disconnect():
    connected_clients["amount"] -= 1


@socketio.on('text_update')
def handle_text_update(data):
    text = data['text']
    emit('update_text', {'text': text}, broadcast=True)


@socketio.on('pageChange')
def handle_page_change(data):
    # Broadcast the page change event to all connected clients
    emit('pageChange', data, broadcast=True)


if __name__ == '__main__':
    socketio.run(app,host="0.0.0.0", port=os.getenv("PORT", default=5000), allow_unsafe_werkzeug=True)
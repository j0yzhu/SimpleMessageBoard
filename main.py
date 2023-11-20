from flask import Flask, request, Response, render_template, session, redirect
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config["SECRET_KEY"] = "jfurehfieo"
socketio = SocketIO(app)

# message will have an author and a content
class Message:
    def __init__(self, author, content):
        self.author = author
        self.content = content


messages = []

@app.route("/", methods=['POST', 'GET'])
def home():
    return render_template("home.html", messages=messages)

# endpoint for sending messages
@app.route("/message", methods=['POST'])
def send_message():
    author = request.form.get('author')
    content = request.form.get('content')

    print(author)
    print(content)

    messages.append(Message(author, content))
    return redirect('/')

# endpoint for getting a list of messages
@app.route("/message", methods=['GET'])
def get_response():
    return {
        'messages': messages
    }


if __name__ == '__main__':
    socketio.run(app, debug=True)

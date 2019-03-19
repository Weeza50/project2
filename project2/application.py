import os
from flask import *
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False

app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = 'super secret key'
socketio = SocketIO(app)

@app.route("/",methods=["POST" ,"GET"])
def index():
    session.pop('user',None)
    if request.method == "POST":
        session.pop('ch',None)
        session.pop('user',None)
        name = request.form['name']
        ch = request.form["channels"]
        session['user'] = name
        session['ch'] = ch

        return redirect(url_for('chat'))

    return render_template('index.html')

@app.route("/chat",methods=["POST" ,"GET"])
def chat():
    if 'user' in session and 'ch' in session:
        ch = session['ch']
        name = session['user']
        return render_template('chat.html',name=name,ch=ch)

    return "invalid request"

@socketio.on("send message")
def vote(data):
    ch = session['ch']
    name = session['user']
    message = data["message"]
    emit("recive messege",{"message":message,"name":name,"ch":ch},broadcast=True)

app.run(debug=True)
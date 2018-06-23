from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO, join_room, leave_room
from mysql import connectToMySQL
import random, string

app = Flask(__name__)
mysql = connectToMySQL("dojopolls")

app.config["SECRET_KEY"] = "1234567890qwertyuiop"
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/start', methods=["POST", "GET"])
def start_room():
    if request.method == "GET":
        return render_template("create/start.html")
    else:
        # generate a random room code
        room_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        print(room_code)
        
        # save room in db
        #room_created = mysql.query_db(f"INSERT INTO polls (title, admin, password, room_id) VALUES ('{request.form['title']}','{request.form['name']}', '{request.form['password']}', '{room_code}')")


@app.route('/login', methods=["POST"])
def login():
    print(request.form["username"])
    print(request.form["password"])
    return redirect('/')

@socketio.on('create room')
def handle_event(room):
    print("Creating Room: " + room)
    join_room(room)

if __name__ == "__main__":
    socketio.run(app)

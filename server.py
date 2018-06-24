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
        room_created = mysql.query_db(f"INSERT INTO polls (title, admin, password, poll_id) VALUES ('{request.form['title']}','{request.form['name']}', '{request.form['password']}', '{room_code}')")
        if room_created:
            return redirect(f'/options/{room_code}')
        else:
            return redirect('/start')

@app.route('/options/<id>')
def add_options(id):
    return render_template('create/add_options.html', room=id)

@app.route('/save/<id>', methods=["POST"])
def save_poll(id):
    query = "INSERT INTO options (description, poll_id) VALUES"
    count = 0
    saved = 0
    for opt in request.form:
        if opt != 'id':
            count += 1
            if mysql.query_db(f"{query} ('{opt}','{id}');"):
                saved += 1
    return "saved" if saved == count else "not saved"

@app.route('/login', methods=["POST"])
def login():
    print(request.form["username"])
    print(request.form["password"])
    return redirect('/')

# @socketio.on('create room')
# def handle_event(room):
#     print("Creating Room: " + room)
    # join_room(room)

if __name__ == "__main__":
    socketio.run(app)
    # app.run(debug=True)
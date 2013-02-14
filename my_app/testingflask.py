# This is where you testing flask exercise goes
# Name: Jessie Daubner

from flask import Flask
app = Flask(__name__)

"""user will be routed to homepage with /"""
@app.route("/")
def hello():
   return "Hello Internet!"

"""infinite loop that runs the app if name is __main__"""
if __name__ == "__main__":
   app.run() 
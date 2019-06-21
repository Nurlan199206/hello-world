# The Docker image contains the following code
from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():
<<<<<<< HEAD
    html = "<h3>Hello, World v1.0!</h3>"
=======
    html = "<h3>Hello, World v.0!</h3>"
>>>>>>> 3c6ee8ca7979629faacd72e80e7e8a996a78923f
    return html

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)


from flask import Flask

# We create an object (our app) of the class Flask 
app = Flask(__name__)

# We are registering a route
@app.route('/')
# This function defines what happens when someone accesses the URL defined by the route above. Function must return something (typically, html, text or JSON)
def hello_world(): 
  return 'Hello, world!'


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True) 


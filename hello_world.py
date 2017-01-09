from flask import Flask # You import the Flask class. This will be the basis of the application
from os import environ # You then import the environ dictionary from os to get access to environment variables from Cloud9

app = Flask(__name__) # Then you create an instance of the class called app, passing in the __name__ variable to tell the app where it is being run from

# This function is decorated twice using the app.route method. This method is used to decorate every Flask view.
# It says that when you visit either the root URL '/' or the /hello URL of the Flask application, the say_hi function should run.
@app.route("/")
@app.route("/hello")
def say_hi(): # Next you create a function called say_hi, which returns the string "Hello World!"
    return "Hello World!"

# Here you change the route slightly to /hello/<name> The <name> part of this is a placeholder, 
# which will take a string and forward it to the view function as a keyword argument
# Notice the added name argument to the view function so you can accept this string
# Then in our hi_person view you simply return a formatted string which contains name.title()

@app.route("/hello/<name>")
def hello_person(name):
    html = '''
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of Molly.  Awww...
        </p>
        <img src="http://s19.postimg.org/av8g0fvvn/image.png">
    '''
    return html.format(name.title())
    
@app.route("/jedi/<first>/<last>")
def jedi_name(first, last):
    jedi = last[0:3] + first[0:2]
    html = '''
    <h1>
        Hello {} {}!
    </h1>
    <p>
        Your Jedi name is {}
    </p>
    <p>
        May the force be with you!
    </p>
    '''
    return html.format(first.title(), last.title(), jedi.title())
    
if __name__ == "__main__": # In the main block you run the application using the app.run method
    app.run(host=environ['IP'], # You use the host and port arguments to tell the application to listen on the values from the Cloud9 workspace environment
        port=int(environ['PORT']))



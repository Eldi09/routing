from flask import Flask, render_template, redirect  # Import Flask to allow us to create our app
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    return render_template('index.html')  # Return the string 'Hello World!' as a response

@app.route('/dojo')
def dojo():
    return "Dojo!"

@app.route('/say/<string:name>')
def sayHi(name):
    return f'Hi {name}'

@app.route('/repeat/<int:num>/<string:name>')
def repeat(num, name):
    return f'{name} ' * num

@app.errorhandler(404)
def error(e):
    return 'Sorry! No response. Try again.'

if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.



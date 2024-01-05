
from flask import Flask, render_template

app = Flask(__name__)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

# Additional routes can be added here

if __name__ == '__main__':
    app.run(debug=True)

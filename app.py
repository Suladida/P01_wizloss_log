from flask import Flask, render_template

app = Flask(__name__)

from controllers import wizards_controller

if __name__ == '__main__':
    app.run(debug=True)
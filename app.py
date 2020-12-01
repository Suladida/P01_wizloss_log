from flask import Flask, render_template
from controllers import wizards_controller
from controllers.wizards_controller import wizards_blueprint

app = Flask(__name__)

app.register_blueprint(wizards_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
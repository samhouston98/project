from flask import Flask, render_template

from controllers.teams_controller import teams_blueprint
from controllers.results_controller import results_blueprint

app = Flask(__name__)

app.register_blueprint(teams_blueprint)
app.register_blueprint(results_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, blueprints
from routes.routes import routes_blueprint
import os

app = Flask(__name__, template_folder='templates')
app.secret_key = "LOLPRIME"


app.register_blueprint(routes_blueprint)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
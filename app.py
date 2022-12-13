import os
import config
from flask import Flask, render_template,request,jsonify,make_response
from auth.routes import auth_bp
from encuestas.routes import encuesta_bp
from extensions.extensions import db

app = Flask(__name__)

#Configuration
app.config.from_object(config.ProdConfig)

#Blueprints
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint()

#SQL
db.init_app(app=app)

@app.route('/')
def home():
    pass

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
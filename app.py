from flask import Flask
from config import Config
from flask_session import Session
import logging
from backend.utils.json_encoder import CustomJSONEncoder

# Create Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Setup session
Session(app)

# Setup logging (optional, can be improved)
logging.basicConfig(level=logging.DEBUG)

# Register blueprints
from backend.routes.auth import auth_bp
from backend.routes.dashboard import dashboard_bp
from backend.routes.interview import interview_bp

app.register_blueprint(auth_bp)
app.register_blueprint(dashboard_bp)
app.register_blueprint(interview_bp)

# Set custom JSON encoder
app.json_encoder = CustomJSONEncoder

if __name__ == '__main__':
    print('\nApp running! Open http://localhost:5000/ in your browser.\n')
    app.run(host='0.0.0.0', port=5000, debug=True)
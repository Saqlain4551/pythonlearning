from flask import Flask
from db.database import db
from routes.auth_routes import auth_bp  # ✅ Make sure this import is here

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///socialmedia.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_secret_key'

db.init_app(app)

# ✅ This line registers your /auth/register route
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

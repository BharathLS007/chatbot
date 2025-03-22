from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Bharath@1@localhost/medical_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

try:
    with app.app_context():
        db.session.execute("SELECT 1")
    print("✅ Database Connected Successfully!")
except Exception as e:
    print("❌ Database Connection Failed:", e)

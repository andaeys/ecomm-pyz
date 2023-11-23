import time

from app import app, db
from flask_migrate import Migrate

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Initialize database
with app.app_context():
    try:
        time.sleep(1)
        db.create_all()
        migrate.init_app(app)
        migrate.upgrade()
        print("db Tables created successfully")
    except Exception as e:
        print(f"db Error creating tables: {e}")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

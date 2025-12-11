from sqlalchemy import text
from app import app, db

with app.app_context():
    try:
        with db.engine.connect() as conn:
            conn.execute(text("ALTER TABLE \"user\" ALTER COLUMN password TYPE VARCHAR(500);"))
            conn.commit()
        print("Updated password column length to 500.")
    except Exception as e:
        print(f"Migration failed: {e}")

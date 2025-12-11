import time
from sqlalchemy import text
from app import app, db

with app.app_context():
    retries = 5
    while retries > 0:
        try:
            # Try to add the column. If it exists, it will fail, which is fine.
            with db.engine.connect() as conn:
                conn.execute(text("ALTER TABLE \"user\" ADD COLUMN is_admin BOOLEAN DEFAULT FALSE;"))
                conn.commit()
            print("Added is_admin column.")
            break
        except Exception as e:
            print(f"Migration info (might already exist): {e}")
            break

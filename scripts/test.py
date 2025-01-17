from sqlalchemy import create_engine

DB_URI = ""


try:
    engine = create_engine(DB_URI)
    connection = engine.connect()
    print("Connection successful!")
except Exception as e:
    print(f"Error: {e}")

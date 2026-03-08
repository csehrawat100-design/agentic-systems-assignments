from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///./student.db"

engine = create_engine(DATABASE_URL, echo=True)

print("tables.py is running...")

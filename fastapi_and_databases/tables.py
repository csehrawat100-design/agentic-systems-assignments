from db import engine
from sqlalchemy import MetaData, Column, Integer, String, CheckConstraint, Table

metadata = MetaData()

students = Table(
    "students",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("age", Integer),
    Column("city", String(100), nullable=True),
    CheckConstraint("age >= 18", name="age_check")
)

metadata.create_all(engine)

print("tables.py is running...")


from .db import engine
from .tables import students
from sqlalchemy import insert, select, update, delete 

def create_student(name: str, age: int, city: str):
    with engine.connect() as connection:
        stmt = insert(students).values(name=name, age=age, city=city)
        connection.execute(stmt)
        connection.commit()

def get_all_students():
    with engine.connect() as connection:
        stmt = select(students)
        return connection.execute(stmt).fetchall()

def update_student_city(student_name: str, new_city: str):
    with engine.connect() as connection:
        stmt = update(students).where(students.c.name == student_name).values(city=new_city)
        connection.execute(stmt)
        connection.commit()

def  delete_students_age_less_than_age(student_age: int):
    with engine.connect() as connection:
        stmt = delete(students).where(students.c.age < student_age)
        connection.execute(stmt)
        connection.commit()

print("crud_opration.py is running...")

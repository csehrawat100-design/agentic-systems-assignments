from .crud_opration import create_student, get_all_students, update_student_city, delete_students_age_less_than_age

# Create new students
create_student("Alice", 22, "New York") 
create_student("Rahul", 25, "Los Angeles")
create_student("Charlie", 19, "Chicago")  # This will fail due to the age constraint

# Retrieve all students
all_students = get_all_students()
for student in all_students:
    print(student)

# Update a student's city
update_student_city("Rahul", "San Francisco")

# Delete students under a certain age
delete_students_age_less_than_age(20)
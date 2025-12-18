import pandas as pd

# 1. Create the DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [20, 22, 19, 21, 20],
    'Grade': ['A', 'B', 'A', 'C', 'B'],
    'Marks': [85, 78, 92, 65, 74]
}

students_data = pd.DataFrame(data)

# 2. Access Data
# Display the first 3 rows
first_three = students_data.head(3)

# Select "Name" and "Marks" columns
name_marks = students_data[['Name', 'Marks']]

# Filter for students with Grade 'A'
grade_a_students = students_data[students_data['Grade'] == 'A']

# --- Displaying Results ---
print("First 3 Rows:")
print(first_three)
print("\nName and Marks Only:")
print(name_marks)
print("\nStudents with Grade A:")
print(grade_a_students)
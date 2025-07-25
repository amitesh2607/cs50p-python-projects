student_records = {
    "Alice": [80, 90, 100],
    "Bob": [70, 75, 85],
    "Carol": [95, 90, 85]
}

for name, grades in student_records.items():
    average = float(sum(grades) / len(grades))
    print(f"{name}: {average}")









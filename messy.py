# -*- coding: utf-8 -*-
"""Print a class report: each student's total, average, and grade, then class average and topper."""

# Each student record is [name, score1, score2, score3]
NAME_INDEX = 0
SCORE_COUNT = 3

students = [
    ["Rahul", 78, 88, 92],
    ["Priya", 65, 71, 69],
    ["Amit", 90, 94, 85],
    ["Sneha", 55, 60, 58],
    ["Vikram", 82, 79, 88],
]


def total_score(student):
    """Sum every score after the name."""
    return sum(student[1:])


def average_score(student):
    """Average using SCORE_COUNT, matching the original fixed divisor of 3."""
    return total_score(student) / SCORE_COUNT


def grade_from_average(average):
    """Letter grade from the same cutoffs as the original script."""
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


print("REPORT")

sum_of_averages = 0
highest_average = 0
topper_name = ""

for student in students:
    total = total_score(student)
    average = average_score(student)
    grade = grade_from_average(average)
    name = student[NAME_INDEX]

    print(f"{name}{total}{average}{grade}")

    sum_of_averages += average
    if average > highest_average:
        highest_average = average
        topper_name = name

class_average = sum_of_averages / len(students)
print(f"Class average:{class_average}")
print(f"Topper:{topper_name}{highest_average}")

# -*- coding: utf-8 -*-
"""Print each student's total, average, and grade, plus the class average and topper."""

NAME_INDEX = 0
FIRST_SCORE_INDEX = NAME_INDEX + 1
SCORE_COUNT = 3

# Each record contains a student's name followed by three scores.
students = [
    ["Rahul", 78, 88, 92],
    ["Priya", 65, 71, 69],
    ["Amit", 90, 94, 85],
    ["Sneha", 55, 60, 58],
    ["Vikram", 82, 79, 88],
]


def total_score(student):
    """Return the sum of a student's scores."""
    scores = student[FIRST_SCORE_INDEX:]
    return sum(scores)


def average_score(student):
    """Return the average of a student's three scores."""
    return total_score(student) / SCORE_COUNT


def grade_from_average(average):
    """Return the letter grade for an average using the original cutoffs."""
    if average >= 90:
        return "A"
    if average >= 80:
        return "B"
    if average >= 70:
        return "C"
    if average >= 60:
        return "D"
    return "F"


def main():
    """Calculate and print the student report and class summary."""
    print("REPORT")

    sum_of_averages = 0
    highest_average = 0
    topper_name = ""

    for student in students:
        name = student[NAME_INDEX]
        total = total_score(student)
        average = average_score(student)
        grade = grade_from_average(average)

        # Keep the original report output format unchanged.
        print(f"{name}{total}{average}{grade}")

        sum_of_averages += average
        if average > highest_average:
            highest_average = average
            topper_name = name

    class_average = sum_of_averages / len(students)
    print(f"Class average:{class_average}")
    print(f"Topper:{topper_name}{highest_average}")


if __name__ == "__main__":
    main()

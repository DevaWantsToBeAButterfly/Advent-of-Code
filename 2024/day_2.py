from aocd import submit
from aocd.models import Puzzle

puzzle_input = Puzzle(2024, 2).input_data.splitlines()

reports = [[int(num) for num in line.split()] for line in puzzle_input]
safe_reports = 0

def check_if_safe(report):
    is_safe = True
    sorted_report = [num for num in report]
    rev_sorted_report = [num for num in report]

    sorted_report.sort()
    rev_sorted_report.sort(reverse=True)

    if report == sorted_report or report == rev_sorted_report:
        for n in range(1, len(report)):
            if abs(report[n] - report[n-1]) < 1 or abs(report[n] - report[n-1]) > 3:
                is_safe = False
    else:
        is_safe = False

    if is_safe:
        return(True)

for report in reports:
    if check_if_safe(report):
        safe_reports += 1

submit(safe_reports, 'a')

safe_reports = 0

for report in reports:
    for n in range(len(report)):
        new_report = [num for num in report]
        new_report.pop(n)
        if check_if_safe(new_report):
            safe_reports += 1
            break

submit(safe_reports, 'b')
reports = open('data.txt').readlines()

safe_reports = []

for report in reports:
    levels = list(map(int, report.split()))

    decreasing = all(levels[i] < levels[i + 1] and 1 <= abs((levels[i] - levels[i + 1])) <= 3 for i in range(len(levels) - 1))
    increasing = all(levels[i] > levels[i + 1] and 1 <= abs((levels[i] - levels[i + 1])) <= 3 for i in range(len(levels) - 1))

    if decreasing or increasing:
        safe_reports.append(levels)

print(len(safe_reports))
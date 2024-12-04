reports = open('data.txt').readlines()

safe_reports = []
unsafe_reports = []


def first_part():
    for report in reports:
        levels = list(map(int, report.split()))

        if all(levels[i] < levels[i + 1] and 1 <=
               abs((levels[i] - levels[i + 1])) <= 3 for i in range(len(levels) - 1)):
            safe_reports.append(levels)
        elif all(levels[i] > levels[i + 1] and 1 <=
                 abs((levels[i] - levels[i + 1])) <= 3 for i in range(len(levels) - 1)):
            safe_reports.append(levels)
        else:
            unsafe_reports.append(levels)

    print(len(safe_reports))


def second_part():
    for report in unsafe_reports:
        for i in range(len(report)):
            new_report = report.copy()
            new_report.pop(i)
            if all(new_report[i] < new_report[i + 1] and 1 <=
               abs((new_report[i] - new_report[i + 1])) <= 3 for i in range(len(new_report) - 1)):
                safe_reports.append(new_report)
                break
            elif all(new_report[i] > new_report[i + 1] and 1 <=
                     abs((new_report[i] - new_report[i + 1])) <= 3 for i in range(len(new_report) - 1)):
                safe_reports.append(new_report)
                break

    print(len(safe_reports))


first_part()
second_part()

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    marks = 0
    avg = 0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for k, v in student_marks.items():
        if k == query_name:
            marks += sum(v)
            avg = marks/3
            print("%.2f" % avg)


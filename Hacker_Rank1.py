if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    total_marks = sum(student_marks[query_name])
    avg_marks = total_marks / len(student_marks[query_name])
    print(f'{avg_marks:.2f}')

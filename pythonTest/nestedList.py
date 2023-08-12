if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
        
    uniqueScore= sorted(set([score for name, score in students]))
    # sorted(uniqueScore)
    name = sorted([name for name,score in students if score == uniqueScore[1]])
    for n in name:
        print(n)

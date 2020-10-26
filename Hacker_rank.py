if __name__ == '__main__':
    score_board = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_board.append([name, score])
    score_board.sort(key=lambda x: (x[1],x[0]))
    names = [i[0] for i in score_board]
    scores = [i[1] for i in score_board]
    min_score = min(scores)
    while scores[0] == min_score:
        scores.remove(scores[0])
        names.remove(names[0])
    for x in range(len(scores)):
        if scores[x]== min(scores):
            print(names[x])    

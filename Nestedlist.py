if __name__ == '__main__':
    scorelist = []
    marksheet = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheet += [[name, score]]
        scorelist += [score]
 #creating dictionary and then converting into back to list, since dict cannot have duplicate
#keys, s making scores as keys and sorting them.
    scorelist = list(dict.fromkeys(scorelist))
    b = sorted(scorelist)[1]
    for a, c in sorted(marksheet):
        if b == c:
            print(a)
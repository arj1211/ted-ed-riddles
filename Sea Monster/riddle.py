# a program to solve the sea monster riddle, https://www.youtube.com/watch?v=YytHuow4VnU

import json
import pathlib
y_possibilities = range(100, 999)
x_possibilies = [1001*y for y in y_possibilities]
patterns = ['ABABAB', 'ACDDCA', 'EEFFDD', 'CGECGE', 'HACACH']
dic_of_patterns = {i: {'count': 0, 'nums': []} for i in patterns}


def check_all_patterns(l):
    for pattern in patterns:
        p = [c for c in pattern]
        count = check_nums_for_p(l, p)
        dic_of_patterns[pattern]['count'] = count
        if count > 0:
            print(pattern, 'has', count, 'solution(s)')


def check_nums_for_p(l, p):
    count = 0
    for num in l:
        dic = {i: -1 for i in p}
        follows_pattern = True
        for i in range(6):  # checking num for pattern
            n = num//(10**(5-i))
            n = n % 10
            if dic[p[i]] == -1 or dic[p[i]] == n:
                dic[p[i]] = n
            else:
                follows_pattern = False
                break
        for c in p:
            for e in p:
                if dic[c] == dic[e] and c != e:
                    follows_pattern = False
        if follows_pattern:
            count += 1
            dic_of_patterns[''.join(p)]['nums'].append(num)
    return count


check_all_patterns(x_possibilies)

with open(str(pathlib.Path(__file__).parent.absolute())+'/riddle.json', 'w') as fp:
    json.dump(dic_of_patterns, fp)

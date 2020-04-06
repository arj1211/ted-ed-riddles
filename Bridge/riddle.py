# a program to solve the bridge riddle, https://www.youtube.com/watch?v=7yDmGnA8Hw0

from itertools import combinations
# givens (assume numbers are unique)
ME = 1  # minute
LABASST = 2  # minutes
JANITOR = 5  # minutes
PROF = 10  # minutes
total_time_available = 17  # minutes
# vars
solved = False  # was a solution found
time_taken = 0  # time used so far
## people on the starting side of the bridge
people_left = [ME, LABASST, JANITOR, PROF]
people_crossed = []  # people on the ending side of the bridge
steps = []  # steps taken for the solution, in words


def solve(time_taken, people_left, people_crossed, steps):
    global solved
    if solved is True:
        return True
    if time_taken > total_time_available:
        return False
    if len(people_left) == 0:
        print('SOLVED!')
        solved = True
        print('~'*10)
        print('Time taken:', time_taken, 'minutes')
        print('Steps:')
        for i in steps:
            print(i)
        return True
    pairs = [x for x in list(combinations(people_left, 2))]
    for P in pairs:
        # case: one pair left; both people go nobody returns
        if len(pairs) == 1:
            if solve(time_taken + max(P), [], people_crossed + [P],
                     steps + [str(P) + ' crosses']):
                return True
            else:
                return False
        # cases: P crosses, someone from people_crossed OR P comes back
        for C in people_crossed+[x for x in P]:
            # first arg: time of slowest in P, time of C returning
            # second arg: people_left after this round trip
            # third arg: people_crossed after C comes back
            if solve(time_taken + max(P) + C,
                     [x for x in people_left if x not in P] + [C],
                     [x for x in people_crossed+[x for x in P] if x != C],
                     steps + [str(P) + ' crosses, ' + str(C) + ' comes back']):
                return True
    # case: no pairs left --> just one person left
    if len(pairs) == 0:
        if solve(time_taken + people_left[0],
                 [], people_crossed + [people_left[0]],
                 steps + [str(people_left[0]) + ' crosses']):
            return True
        else:
            print('no solution')
            return False


# solve(0, [ME, LABASST, JANITOR, PROF], [], [])
solve(time_taken, people_left, people_crossed, steps)

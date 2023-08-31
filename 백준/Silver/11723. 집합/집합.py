import sys

S = set()

for _ in range(int(sys.stdin.readline())):
    order = sys.stdin.readline().strip().split()

    if len(order) == 1:
        # all, empty
        if order[0] == "all":
            S = set([i for i in range(1, 20+1)])
        else:
            S = set()

    else:
        function, number = order[0], order[1]
        number =  int(number)

        if function == "add":
            S.add(number)
        elif function == "remove":
            S.discard(number)
        elif function == "check":
            if number in S:
                print(1)
            else:
                print(0)
        elif function == "toggle":
            if number in S:
                S.discard(number)
            else:
                S.add(number)
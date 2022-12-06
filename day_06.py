last_4 = []
done_4 = False
last_14 = []

with open("inputs/day_06.txt", "r") as f:
    i = 0
    while True:
        i += 1

        char = f.read(1)
        if not char:
            break

        if not done_4:
            last_4.append(char)
            if len(last_4) > 4:
                last_4.pop(0)
            if len(set(last_4)) == 4:
                print(i)
                done_4 = True

        last_14.append(char)
        if len(last_14) > 14:
            last_14.pop(0)
        if len(set(last_14)) == 14:
            print(i)
            break

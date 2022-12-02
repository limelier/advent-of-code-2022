# Day 2
# this day really seems like it could be done better at first glance
# but after looking into it more, no, mapping all inputs to all outputs directly really seems optimal

shape_scores = {"rock": 1, "paper": 2, "scissors": 3}
result_scores = {"loss":  0, "tie": 3, "win": 6}

mapping_1 = {
    "A": {  # rock
        "X": ("rock", "tie"),
        "Y": ("paper", "win"),
        "Z": ("scissors",  "loss"),
    },
    "B": {  # paper
        "X": ("rock", "loss"),
        "Y": ("paper", "tie"),
        "Z": ("scissors", "win"),
    },
    "C": {  # scissors
        "X": ("rock", "win"),
        "Y": ("paper", "loss"),
        "Z": ("scissors", "tie"),
    }
}

mapping_2 = {
    "A": {  # rock
        "X": ("loss", "scissors"),
        "Y": ("tie", "rock"),
        "Z": ("win", "paper"),
    },
    "B": {  # paper
        "X": ("loss", "rock"),
        "Y": ("tie", "paper"),
        "Z": ("win", "scissors"),
    },
    "C": {  # scissors
        "X": ("loss", "paper"),
        "Y": ("tie", "scissors"),
        "Z": ("win", "rock"),
    }
}

score_sum_1 = 0
score_sum_2 = 0
with open("inputs/day_02.txt", "r") as f:
    for line in f.readlines():
        line = line.strip()
        left, right = line.split(" ")

        shape_1, result_1 = mapping_1[left][right]
        score_sum_1 += shape_scores[shape_1] + result_scores[result_1]

        result_2, shape_2 = mapping_2[left][right]
        score_sum_2 += shape_scores[shape_2] + result_scores[result_2]

print("Part 1:", score_sum_1)
print("Part 2:", score_sum_2)

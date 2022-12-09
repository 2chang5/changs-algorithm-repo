import sys

sentence = sys.stdin.readline().rstrip().split(" ")

front = ["c", "j", "n", "m", "t", "s", "l", "d", "qu"]
mo = ["a", "e", "i", "o", "u", "h"]

hypenProcessedSentence = []

for i in sentence:
    if "-" in i:
        temp = i.split("-")
        hypenProcessedSentence.extend(temp)
    else:
        hypenProcessedSentence.append(i)

conclusionSentence = []

for i in hypenProcessedSentence:
    if "'" in i:
        temp = i.split("'")
        if temp[0] in front and temp[1][0] in mo:
            conclusionSentence.extend(temp)
        else:
            conclusionSentence.append(i)
    else:
        conclusionSentence.append(i)

print(len(conclusionSentence))

# 왜 틀렸는지 모르겠다 진짜 안해 더러운문

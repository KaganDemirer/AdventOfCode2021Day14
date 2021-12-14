rules = {}
pairs = {}
how_often = {}

with open("14_Advent.txt") as input_files:
    lines = input_files.readlines()
    for x in lines:
        if x.replace("\n","") == "":
            continue
        elif "->" in x:
            a,b = x.replace("\n","").split(" -> ")
            rules[a] = b
        else:
            input = x.replace("\n","")
            for x in range(len(input)-1):
                try:
                    pairs[f"{input[x]}{input[x+1]}"] = pairs[f"{input[x]}{input[x+1]}"] + 1
                except:
                    pairs[f"{input[x]}{input[x+1]}"] = 1

def new_step():
    t = {}
    for x in pairs.keys():
        rep = rules[x]
        try:
            t[f"{x[0]}{rep}"] = t[f"{x[0]}{rep}"] + pairs[x]
        except:
            t[f"{x[0]}{rep}"] = pairs[x]
        try:
            t[f"{rep}{x[1]}"] = t[f"{rep}{x[1]}"] + pairs[x]
        except:
            t[f"{rep}{x[1]}"] = pairs[x]
        try:
            how_often[rep] = how_often[rep] + pairs[x]
        except:
            how_often[rep] = pairs[x]
    return t

for _ in range(40):
    pairs = new_step()
print(how_often[max(how_often, key=how_often.get)] - how_often[min(how_often, key=how_often.get)]+1)
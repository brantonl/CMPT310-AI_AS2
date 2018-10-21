import sys

def extract(str, delim):
    data = []
    for i in str:
        if i in delim:
            continue
        data.append(i)
    return data
    
def checkBody(first_g, rule):
    #check p <- p,q
    if(first_g in rule[1:len(rule)]):
        return False
    #check p->q then q->p
    elif(len(steps) > 0 and len(rule) == 2 and len(steps[len(steps)-1]) ==2 and steps[len(steps)-1][0] == rule[1] and steps[len(steps)-1][1] == rule[0]):
        return False
    return True

def combine(glist, rlist):
    for i in range(len(rlist)):
        if(rlist[i] not in glist):
            glist.append(rlist[i])
    return glist

def solve(goals):
    if(len(goals) == 0):
        return True
    else:
        first_goal = goals.pop(0)
        for r in range(len(rules)):
            #check for match header and then check the body
            if(rules[r][0] == first_goal and checkBody(first_goal, rules[r])):
                steps.append(rules[r])
                #print("first goal:{0}, append step:{1}".format(first_goal, rules[r]))
                goals = combine(goals, rules[r][1:len(rules[r])])
                if(solve(goals)):
                    return True
        return False

rules = []
steps = []
delim = "[], \n"
if len(sys.argv) < 2:
   print("Please enter the file name to input the set of rules.\n")
else:
    with open(sys.argv[1]) as f:
        for line in f:
            rules.append(extract(line, delim))
        f.close

target = input("Please enter the query of an atom: ")
g_list = [target]

print("\nlist of rules: ")
for j in range(len(rules)):
    print(rules[j])

if(solve(g_list)):
    steps.reverse()
    print("\n" + target + " is a logical consequence of the set of rules.\n\nsteps taken to derive a valid chain of reasoning: ")
    for i in range(len(steps)):
        print(steps[i])
        if(steps[i][0] == target):
            break
else:
    print("\n" + target + " is not a logical consequence of the set of rules.\n\nsteps taken till chain of reasoning fails:")
    if(len(steps)>0):
        for i in range(len(steps)):
            print(steps[i])
    else:
        print("no steps taken in backward chaining")
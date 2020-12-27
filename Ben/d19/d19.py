
def solve(line):
    # print("top string=", line)
    match_indexes = match(line)
    # if match_indexes matched the whole string
    return len(line) in match_indexes

# Credit to
# https://github.com/mebeim/aoc/blob/master/2020/README.md#day-19---monster-messages
def match(input_str, rule='0', match_start=0):
    # if starting past the string, return no matches
    if match_start >= len(input_str):
        return []

    # get rule rhs from rule number
    rule = rule_list[rule]
    # rule = list for non-terminals, str for terminals
    if type(rule) is str:
        # if head of input string matches rule terminal symbol
        if input_str[match_start] == rule:
            return [match_start+1]
        # else return no match indexes
        return []
    
    matches = []
    for option in rule:
        submatches = [match_start]
        for sub_rule in option:
            new_matches = []
            for submatch_pos in submatches:
                new_matches += match(input_str, sub_rule, submatch_pos)
            submatches = new_matches
        matches += submatches
    return matches

rule_list = {}
with open("input.txt", "r") as f:
    data = f.read()
    rules, data = [part.split('\n') for part in data.split('\n\n')]
    rules = [(r[0], r[1]) for r in [line.split(': ') for line in rules]]

    # convert rule numbers into rule indexes
    for (idx,rhs) in rules:
        line_rule = []
        rhs = rhs.split(' | ')
        if rhs[0][0] in set('1234567890'):
            # non-terminal rule reference
            for part in rhs:
                part = part.split(' ')
                line_rule.append(part)
                continue
        else:
            # letter terminal
            line_rule = rhs[0][1]
        rule_list[idx] = line_rule

    # run solver on data
    p1 = sum([solve(line) for line in data])
    print(p1)

    # 8: 42 | 42 8
    # 11: 42 31 | 42 11 31
    rule_list['8']  = [['42'],['42','8']]
    rule_list['11'] = [['42','31'],['42','11','31']]
    # rule_list[8]  = [[42]]+ [[42]*i for i in range(1,11)]
    # rule_list[11] = [[42]*i+[31]*i for i in range(1,11)]
    p2 = sum([solve(line) for line in data])
    print(p2)


def solve(line):
    # print("top string=", line)
    passfail,remaining = match_or(new_rules[0], line)
    if passfail and not remaining:
        print('pass', line)
    # remaining strings are fails
    return passfail and not remaining

def match_or(rule, line):
    pos = line
    rule_pass = False
    for rp in rule:
        rule_pass,line_nxt = match_sequence(rp, line)
        if rule_pass:
            # print('Rule match',rp,line,'->',line_nxt)
            pos = line_nxt
            break
        # print('Rule mismatch',rp,line,'->',line_nxt)
    return rule_pass,pos

def match_sequence(rule, line):
    r_pass = False
    for r in rule:
        rr = new_rules[r]
        # match A|B
        if type(rr) is list:
            r_pass,pos = match_or(rr, line)
            if not r_pass:
                break
            line = pos
        # Match terminal symbol
        else:
            # terminal letter, so check it matches line[0]
            r_pass = line[0] == rr
            if not r_pass:
                break
            line = line[1:]
    return r_pass,line

new_rules = {}
with open("input.txt", "r") as f:
    data = f.read()
    rules, data = [part.split('\n') for part in data.split('\n\n')]
    rules = [(int(r[0]), r[1]) for r in [line.split(': ') for line in rules]]

    # convert rule numbers into rule indexes
    for (idx,rhs) in rules:
        line_rule = []
        print((idx,rhs))
        rhs = rhs.split(' | ')
        if rhs[0][0] in set('1234567890'):
            # non-terminal rule reference
            for part in rhs:
                part = list(map(int, part.split(' ')))
                line_rule.append(part)
                continue
        else:
            # letter terminal
            line_rule = rhs[0][1]
        new_rules[idx] = line_rule

    # run solver on data
    p1 = sum([solve(line) for line in data])
    print(p1)


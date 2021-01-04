def solve(s):
    if 0 < len(s) < 1000:
        lst = [word[0].upper() + word[1:] for word in s.split()]
        s = " ".join(lst)
    return s
def solve(s):
    return re.sub("(^|\s)(\S)", lambda m: m.group(1) + m.group(2).upper(), s)

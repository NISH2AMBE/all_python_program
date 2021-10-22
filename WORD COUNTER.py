# WORD COUNTER

def world_founder(s):
    a = {}
    for char in s:
        a[char] = s.count(char)
    return a

print(world_founder("PATEL VIJAYKUMAR KESHAVLAL"))
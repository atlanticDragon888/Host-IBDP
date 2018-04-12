def compress(s):
    run = ""
    length = len(s)
    if length == 0:
        return ""
    if length == 1:
        return s + "1"
    last = s[0]
    cnt = 1
    i = 1
    while i < length:
        if s[i] == s[i - 1]: # check it is the same letter
            cnt += 1
        else:
            run = run + str(s[i - 1]) + str(cnt) # if not, store the previous data
            cnt = 1
        i += 1
    run = run + str(s[i - 1]) + str(cnt)
    bits = bin(int.from_bytes(run.encode('utf-8', 'surrogatepass'), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def decompress(s):
    n = int(s, 2)
    s = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode('utf-8', 'surrogatepass') or '\0'
    newdat = []
    range1 = range(0, len(s), 2)
    range2 = range(1, len(s), 2)
    for i in range(len(range2)):
        newdat.append(str(s[range1[i]]) * int(s[range2[i]]))
    return ''.join(newdat)
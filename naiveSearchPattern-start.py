# naive search pattern - complexity depends on algorithm
# Naive Search Pattern-O(m*(n-m))-----(n-length of text,m=length of pattern)

def naiveSearch(pat, txt):
    m = len(pat)
    n = len(txt)
    for i in range(n-m+1):  # 19-4+1
        j = 0
        while j < m:
            if txt[i+j] != pat[j]:
                break
            j += 1
        if j == m:
            print('patten found at', i)


txt = 'AABAACAADAABCAAABAA'  # 19
pat = 'AA'  # 4

naiveSearch(pat, txt)  # O(m*(n-m)) complexity depends on algorithm
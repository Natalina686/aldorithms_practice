def naive_search(text, pattern):
    n, m = len(text), len(pattern)
    for i in range(n-m+1):
        if text[i:i+m] == pattern:
            print(f"Pattern found at index {i}")


text = "abcabcabcd"
pattern = "abcab"
naive_search(text, pattern)


def compute_lps(pattern):
    lps = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    return lps


def kmp_search(text, pattern):
    lps = compute_lps(pattern)
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            print(f"Pattern found at index {i - j}")
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


text = "abxabcabcaby"
pattern = "abcaby"
kmp_search(text, pattern)


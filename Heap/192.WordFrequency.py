def frequencySort(self, s: str) -> str:
    frequency = Counter(s)
    n = len(s)
    bucket = [[] for _ in range(n + 1)]
    ans = []

    for char, freq in frequency.items():
        bucket[freq].append(char)

    for i in range(n, 0, -1):
        for ch in bucket[i]:
            ans.append(ch * i)

    return "".join(ans)

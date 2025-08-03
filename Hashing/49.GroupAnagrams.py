def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    answer = []
    hash = {}
    group = 0
    for i in range(len(strs)):
        cur = "".join(sorted(strs[i]))
        if cur in hash:
            answer[hash[cur]].append(strs[i])
        else:
            answer.append([strs[i]])
            hash[cur] = group
            group += 1

    return answer

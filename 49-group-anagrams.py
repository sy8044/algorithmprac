import collections

strs = ["eat","tea","tan","ate","nat","bat"]

dic = collections.defaultdict(list)

for str in strs :
    dic[''.join(sorted(str))].append(str)

print(dic.values())
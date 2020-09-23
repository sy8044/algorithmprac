import re
from collections import deque


s = "A man, a plan, a canal: Panama"

s = s.lower()
s = re.sub('[^a-z]','',s)

queue = deque()

isTrue = True
for i in s :
    queue.append(i)

while len(queue) > 1 :
    left = queue.popleft()
    right = queue.pop()
    if not left == right :
        isTrue = False
        break

print(isTrue)




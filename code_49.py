# question : sorting elements by frequency in an array
from collections import Counter
list1=[10,20,20,40,40,50,50,50]
result=[item for items, c in Counter(list1).most_common() for item in [items] * c]

print(str(result))
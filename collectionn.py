from collections import namedtuple,OrderedDict,defaultdict,ChainMap,Counter,deque
tup = (23,3)
point = namedtuple('Pointer',['x','y'])
p = point(3,3)

print(f'tup == {tup[1]}')
print(f'p == {p[0]}')

#deque
d = deque([1,2,3,3])
d.append(33)

#queue
l = [1,2,23]

l.append(323)
d.appendleft(33)

print(f'dequee == {d}')
print(f'quee == {l}')

#chianmap - used to chain dictionary which are mapable
a =32
left = { a:2,'a':1,'b':3}
right = {'e':32,'d':232,'e':'someting'}
#gather = left+right #it does not work

print(f'left-- {left}')
print(f'right-- {right}')
print(f'items-- {right.items()}')


#chained
chained = ChainMap(left,right)
print(f'chained-gatheres-- {chained}')
print(f'chained-gatheres-- {chained['a']} {left['a']}')


#counter 

count = Counter([1,2,2,3,3])
#count2 = Counter(1,2,2,3,3)
print(f'\ncounter== {count} ')
for c in count.elements():
    print(f'\neach item== {c}')
print(f'\ncounter-elements== {count.elements()} ')

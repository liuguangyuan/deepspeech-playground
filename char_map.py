import keras.backend as K

char_map_str = """
' 1
<SPACE> 2
a 3
b 4
c 5
d 6
e 7
f 8
g 9
h 10
i 11
j 12
k 13
l 14
m 15
n 16
o 17
p 18
q 19
r 20
s 21
t 22
u 23
v 24
w 25
x 26
y 27
z 28
"""


def ctc_idx(i):
    if K.backend() == 'tensorflow':
        return i - 1
    elif K.backend() == 'theano':
        return i
    raise ValueError

char_map = {}
index_map = {}
for line in char_map_str.strip().split('\n'):
    ch, index = line.split()
    i = ctc_idx(int(index))
    char_map[ch] = i
    index_map[i] = ch
index_map[ctc_idx(2)] = ' '

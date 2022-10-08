import heapq
new = {}
fk = []

class node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq

def printNodes(node, val=''):
    newVal = val + str(node.huff)
    if (node.left):
        printNodes(node.left, newVal)
    if (node.right):
        printNodes(node.right, newVal)
    if (not node.left and not node.right):
        # inserts letter and code in dictionary as key value pair
        new[node.symbol] = newVal
        print("\t>>", f"{node.symbol} -> {newVal}")

def encodeMsg(str, edict):
    for i in str:
        for k in edict.keys():
            if (i == k):
                fk.append(edict.get(k))
                print("\t>> ", edict.get(k))
            else:
                continue

def keysevalue(new, v):  # finds key for a value
    value = {i for i in new if new[i] == v}
    return value

def decodeMsg(new, fk):
    for i in fk:
        for v in new.values():
            if (i == v):
                print("\t>>", keysevalue(new, v))

str1 = input("Enter the string:\t")
letters = []
for x in str1:
    if x not in letters:
        frequency = str1.count(x)
        letters.append(x)
        letters.append(frequency)

print("LETTER -> FREQ")
for y in range(0, len(letters), 2):
    print("  ", letters[y], "  ->  ", letters[y+1])
print("\t<> <> <> <> <> <> <> <> <> <> <> <> ")
# print(letters[0])
alpha = []
occur = []
for i in range(0, len(letters)):
    if i % 2:
        occur.append(letters[i])
    else:
        alpha.append(letters[i])
Tnodes = []
for x in range(len(alpha)):
    heapq.heappush(Tnodes, node(occur[x], alpha[x]))

while len(Tnodes) > 1:
    left = heapq.heappop(Tnodes)
    right = heapq.heappop(Tnodes)
    left.huff = 0
    right.huff = 1
    newNode = node(left.freq+right.freq, left.symbol+right.symbol, left, right)
    heapq.heappush(Tnodes, newNode)
print("Table for encoded letters:")
printNodes(Tnodes[0])
print("\n")
endict = new
print("Encoded Message:")
encodeMsg(str1, endict)
print("\n")
print("Decoded Message: ")
decodeMsg(new, fk)
print("\n")

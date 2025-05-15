class node:
    def __init__(self, value, mom, dad):
        self.value = value
        self.mom = mom
        self.dad = dad


n = int(input("Enter num of points\n"))
xis = [0. for _ in range(n)]
newton = [[] for _ in range(n)]
print("Enter points like this, one point at a time:\n3 -2.5\n-1 4")
for i in range(n):
    l = list(map(float, input().split()))
    newton[0].append(node(l[1], l[0], l[0]))
    xis[i] = l[0]

for i in range(1, n):
    previous = newton[i - 1]
    for j in range(len(newton[i - 1]) - 1):
        first = previous[j]
        second = previous[j + 1]
        new_node = node((second.value - first.value) / (second.dad - first.mom), first.mom, second.dad)
        newton[i].append(new_node)

# for a in newton:
#     for b in a:
#         print(b.value, end=" ")
#     print()

coefficient_list = [newton[i][0].value for i in range(len(newton))]

# print(coefficient_list)

x = float(input("Enter the x whose y is required\n"))

fx = coefficient_list[0]
multiplier = x - xis[0]

for i in range(1, len(coefficient_list)):
    fx += coefficient_list[i] * multiplier
    multiplier *= x - xis[i]

print("f(" + str(x) + ")= " + str(fx))

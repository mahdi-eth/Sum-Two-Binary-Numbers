import sys

# getting inputs
x1 = input("Enter the first binary number: ")
x2 = input("Enter the second binary number: ")

# put the larger number into x1
if(x2 > x1):
    x1, x2 = x2, x1

# arrays to store numbers in them
n1 = []
n2 = []

# apeend x1 numbers to n1
for i in range(len(x1)):
    n1.append(int(x1[i]))

# apeend x2 numbers to n2
for j in range(len(x2)):
    n2.append(int(x2[j]))

# defining n1 & n2 lengths
n1_len = len(n1)
n2_len = len(n2)

# exit the program if user entered decimal number
for k in range(n1_len):
    if (n1[k] == 0 or n1[k] == 1):
        continue
    else:
        print("Error: Enter binary number (0 or 1)")
        exit()
for l in range(n2_len):
    if (n2[l] == 0 or n2[l] == 1):
        continue
    else:
        print("Error: Enter binary number (0 or 1)")
        exit()

# defining collector
collector = []

# defining state
adder_state = False

# calculate the sum
for m in range(n1_len):
    if (m <= n2_len):
        tmp = n1[n1_len - m - 1] + n2[n2_len - m - 1]
        if (adder_state):
            tmp += 1
            adder_state = False
    else:
        tmp = n1[n1_len - m - 1]
        if (adder_state):
            tmp += 1
            adder_state = False
    if (tmp >= 2):
        if(m == n1_len - 1):
            if(tmp == 2):
                collector.append(0)
                collector.append(1)
            if(tmp == 3):
                collector.append(1)
                collector.append(1)
            break
        else:
            if(tmp == 2):
                collector.append(0)
            if(tmp == 3):
                collector.append(1)
            adder_state = True
            continue
    collector.append(tmp)

# generating the output
collector = list(reversed(collector))
result = ''.join(str(i) for i in collector)
print(result)

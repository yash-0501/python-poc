str1 = "ABCD"
str2 = "PQR"
for i in range(4):
    for j in range(i + 1):
        print(str1[j], end="")
    for k in range(i, 3):
        print(str2[k], end="")
    print()
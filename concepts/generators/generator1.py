def topTen():
    n = 1
    while(n<=10):
        sq = n*n
        yield sq  #yield doesnt terminate the function like return
        n+=1

val = topTen()

for i in val:
    print(i)

#to create a iterator use a generator
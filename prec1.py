#def collatz(n):   #never success in def
list2 = []
for n in range(1, 10):
    list1 = []
    count = 0
    if n == 1:
        list1.append(n)
        count = 1
    while n > 1:
        if n % 2 == 0:
            n = n/2
        elif n % 2 == 1:
            n = 3*n + 1
        list1.append(n)
        count = count + 1
    #print list1
    #print count
    list2.append(count)
print list2

m = 0
for i in range(len(list2)):
    if list2[i] > m:
        m = list2[i]
        n = i
print m
print n+1

#also never success
#def main():
#if __name__ == "__main__":
#    collatz()

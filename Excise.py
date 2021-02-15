# Enter your code here. Read input from STDIN. Print output to STDOUT
Array = [0 , 1 , 0 , 0]
value = input()
for n in range(len(Array)):
    if Array[n] == 1 and value == "R":
        Array.pop(n)
        Array.insert(n,0)
        Array.pop(n+1)
        Array.insert(n+1,1)
        number = n
    if Array[n] == 1 and value == "L":
        Array.pop(n)
        Array.insert(n,1)
print(Array)
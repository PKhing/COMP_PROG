dict = {
    "Robert" :"Dick",
    "William" :"Bill",
    "James" :"Jim",
    "John" :"Jack",
    "Margaret" :"Peggy",
    "Edward" :"Ed",
    "Sarah" :"Sally",
    "Andrew" :"Andy",
    "Anthony" :"Tony",
    "Deborah" :"Debbie"
}
n = int(input())
for i in range(n):
    x = input()
    ans = ""
    for i in dict.keys():
        if i == x:
            ans = dict[i]
            break
        if dict[i] == x:
            ans = i
            break
    if ans == "":
        print("Not found")
    else:
        print(ans)

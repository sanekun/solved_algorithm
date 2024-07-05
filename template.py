import sys

M, N = map(int, sys.stdin.readline().strip().split())

plate = []
done = True
for _ in range(N):
    tmp = list(map(int, sys.stdin.readline().strip().split()))
    if done:
        if 0 in tmp:
            done = False
    plate.append(tmp)

if done:
    print (0)
    sys.exit()

new_map = sum(plate, [])

cnt = 0

while True:
    
    tomato = [n for n, i in enumerate(new_map) if i ==1]
    ans = set({})
    for i in tomato:
        y = i // M
        x = i % M
        
        if y != N-1:
            ans.add((y+1, x))
        if y != 0:
            ans.add((y-1, x))
        if x != M-1:
            ans.add((y, x+1))
        if x != 0:
            ans.add((y, x-1))
        
    cnt += 1
    
    for i in list(ans):
        y, x = i
        if plate[y][x] == 0:
            plate[y][x] = 1
    
    if sum(plate, []) == new_map:
        if 0 in new_map:
            print (-1)
        else:
            print (cnt-1)
        break
    else:
        new_map = sum(plate, [])
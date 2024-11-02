n = int(input())
balls = input().strip()


move_cnt = []

# R 우측으로 보냄
rrballs = balls.rstrip("R")
move_cnt.append(rrballs.count("R"))

# R 좌측으로 보냄
rlballs = balls.lstrip("R")
move_cnt.append(rlballs.count("R"))

# B 우측으로 보냄
brballs = balls.rstrip("B")
move_cnt.append(brballs.count("B"))

# B 좌측으로 보냄
blballs = balls.lstrip("B")
move_cnt.append(blballs.count("B"))

print(min(move_cnt))
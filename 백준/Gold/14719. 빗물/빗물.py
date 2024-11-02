x, y = map(int, input().split(" "))
block = [int(i) for i in input().split(" ")]
max_index = block.index(max(block))


l_all_width = 0
temp_length=0
l_block_width = 0
for i in range(max_index):
    temp_length = max(temp_length, block[i])
    l_all_width+=temp_length
    l_block_width+=block[i]

    
temp_length = 0
r_all_width = 0
r_block_width = 0
for j in range(len(block)-1, max_index, -1):
    temp_length = max(temp_length, block[j])
    r_all_width+=temp_length
    r_block_width +=block[j]
    
all_width = l_all_width+r_all_width
block_width = l_block_width+r_block_width

print(all_width - block_width)
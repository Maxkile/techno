def getColLen(v,cols):
    col_len_lst = list()
    col_len = 0
    for i in range(0,cols):
        for j in range(i,len(v),cols):
            col_len += 1
        col_len_lst.append(col_len)
        col_len = 0
    return tuple(col_len_lst)
        
def getLineLen(v,cols):
    line_len_lst = list()
    line_len = 0
    for i in range(0,len(v)):
        line_len += 1
        if ((line_len == cols) or (i == len(v)-1)):
            line_len_lst.append(line_len)
            line_len = 0
    return tuple(line_len_lst)
    
def reorder_list(v,cols):
    new_lst = list()
    line_len = getLineLen(v,cols)
    col_len = getColLen(v,cols)
    for i in range(0,col_len[0]):
        j = i
        overall_steps_num = line_len[i]
        prev_step_num = 0
        skip = False
        for step_size in range(col_len[0],0,-1):
                for step_num in range(0,line_len[step_size - 1] - prev_step_num):
                    if (overall_steps_num == 0):
                        skip = True
                        break
                    else:
                        overall_steps_num -=1
                        new_lst.append(v[j])
                        j += step_size
                if skip:
                    break
                else:
                    prev_step_num = line_len[step_size  - 1]
    return new_lst

    # if __name__ == "__main__":





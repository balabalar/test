TOTAL_NUM = 40
CYCLE_NUM = 6
survival_num = [x for x in range(1,TOTAL_NUM)]

def get_rest_list(cycle_num,survival_list):
    survival_list.remove(survival_list[cycle_num-1])
    return(survival_list)
         
def get_survival_list(death_num,rest_list):
    temp = rest_list[death_num - 1:]
    temp.extend(rest_list[0 : death_num - 1])
    return(temp)
    
    
for i in range(TOTAL_NUM - CYCLE_NUM):
    
    rest_num = get_rest_list(CYCLE_NUM,survival_num) 

    survival_num = get_survival_list(CYCLE_NUM,rest_num)

    print(survival_num)
    

    
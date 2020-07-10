import random

NUM_TOTAL = 40
def get_scores(num_total,score_max = 100):
    return([random.randint(0,score_max) for x in range(num_total)])

def filter_under_average(score_list):
    average = (float(sum(score_list)))/len(score_list)
    under_average_scores = [x for x in score_list if x < average]
    return under_average_scores

student_scores = get_scores(NUM_TOTAL)
temp = filter_under_average(student_scores)
print('低于平均分的人数为:%d\t'%len(temp))
rising = True
sort = sorted(student_scores,reverse=rising)
print(sort)
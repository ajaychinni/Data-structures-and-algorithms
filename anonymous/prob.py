from random import randint
def prob_game():
    total_size = 1000
    sample_size1 = 0
    sample_size2 = 0
    prev,curr = None,None
    cost1 = 0
    cost2 = 0
    while sample_size1 < total_size or sample_size2 < total_size:
        prev = curr
        curr = randint(1,6)
        if sample_size1 < total_size:
            cost1 += 1
        if sample_size2 < total_size:    
            cost2 += 1
        if prev == 5 and curr == 6:
            sample_size1 += 1
        if prev == 6 and curr == 6:
            sample_size2 += 1
            
    return cost1/total_size, cost2/total_size 

print(prob_game())  
        
        
         
    
import pandas as pd
import numpy as np


chat_id = 143893840 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
  
    
    #probabilty criterion
    prob_control = x_success / x_cnt
    prob_test = y_success / y_cnt
    
    
    #binom, porbabilty, total_size
    t_test, errors = [], []
    iterations = 10000
    p_value = 0.03
    
    for i in range(iterations):
        
        first = np.random.binomial(1, prob_control, x_cnt)
        second = np.random.binomial(1, prob_test, y_cnt)

        test = ttest_ind(first, second)
        error = abs((np.mean(first) - np.mean(second))
        
        t_test.append(test.pvalue >= p_value)
        errors.append(error)
        
    result = np.mean(t_test)
    errors = np.mean(errors)
    
    return result < p_value

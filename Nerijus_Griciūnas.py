# -*- coding: utf-8 -*-
#Python 3.8
def replace_double(w):
    for i in range(len(w)-1, 0, -1):
        if w[i] == w[i-1]:
            w = w.replace(w[i-1]+w[i-1], w[i])   
    return w

print(replace_double('worrd'))


def replace_pi(w):
    if w == 'pi' :
        w = '3.14'
    return w

print(replace_pi('pienas'))

def replace_double_pi(s):
    words = s.split(' ')
    for w in words:
        replace_double(w)
        replace_pi(w)
    return words

print(replace_double_pi('pi nott py'))
    

#task #2
num=list(range(1, 26))
print(num)

def algo1(n):
    if n[0]%2 == 0:
        return [x for x in n if x%2 == 0]
    else:
        return [x for x in n if x%2 != 0]
        
def algo2(n):
    
    i = 1
    output_list = n
    while len(output_list) >= output_list[i]:
        remove_every = output_list[i]
        output_list = [x for i, x in enumerate(output_list) if (i + 1) % remove_every == 0]
        i = i+1
        
    return output_list
        
print(algo2(algo1(num)))

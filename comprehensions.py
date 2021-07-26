some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

mod=list(set(dup for dup in some_list if some_list.count(dup)>1))
#new_mod=set(mod)
print(mod)
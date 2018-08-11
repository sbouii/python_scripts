
def get_dictionary():
 l = {1:'d', 2:'m'}
 print l.items()
 print l.keys() 
 print l.values() 

def from_list_to_dictionary():
 l = ['m', 'f', 'g']
 d = {}
 i = 0
 for e in l:
  d.update({i:e})
  i = i + 1
 print d

def merge_two_dictionaries():
 l1 = {1:'s', 2:'m', 3:'h'}
 l2 = {1:'h', 2:'d', 3:'a'}
 list1 = l1.items()
 list2 = l2.items()
 l3 = dict(list1 + list2)
 print l3

def map_two_lists_to_dictionary():
 l1 = [1, 2, 3]
 l2 = ['m', 's', 'f']
 print dict(zip(l1,l2)) 


def remove_duplicates_from_list():
 l = [1, 2, 2]
 print list(set(l))

def remove_duplicates_from_dictionary():
 d = {1:'m', 1:'d', 2: 's', 3: 'j'}
 l = list(set(d.items()))
 print dict(l)

def replace_element_at_specific_position_list():
 l = ['l', 'f', 'm']
 l[1] = 'h'
 print l

def insert_at_the_begining_of_list():
 l = ['l', 'f', 'm']
 l[0] = 'h'
 print l

def insert_element_at_specific_position_list():
 l =  ['l', 'f', 'm']
 l.insert(1, 's')
 print l

def get_index_of_element_list():
 l = ['l', 'd', 'k']
 print l.index('d')

def replace_element_at_specific_position_dictionnary():
 d = {1:'f', 2:'s', 3:'m'}
 d['1'] = 'n'
 print d

def get_index_of_element_at_specific_position_dictionary():
 d = {'m': 'd', 'f':'s', 'h':'l'}
 d.keys().index('f')

def insert_element_at_specific_position():
 d = {'a':'a', 'b':'b', 'd':'d'}
 d.update({'c':'c'})
 print d

def delete_element_from_dictionary():
 d = {'m': 'd', 'f':'s', 'h':'l'}
 del d['m']
 print d

def delete_element_from_list():
 l = ['a', 'b', 'c']
 l.remove('a')
 print l

def extend_and_plus():
 l1 = [1,2,3]
 l2 = [5,6,7]
 l1.extend(l2)
 print l1
 l3 = l1 + l2
 print l3

def sort_list():
 l1 = [1,3,2]
 l1.sort()
 print l1

def last(i):
 return i[0] + i[-1]

def sort_list():
 l1 = [(1,3), (2,3), (5,6)]
 l1.sort(key=last)
 print l1

from collections import OrderedDict
def sort_dictionary_key():
 d = {'a': 1, 'b': 2, 'c': 3}
 OrderedDict(sorted(d.items(), key=lambda t: t[0]))

def sort_dictionary_value():
 d = {'a': 1, 'b': 2, 'c': 3}
 OrderedDict(sorted(d.items(), key=lambda t: t[1]))

def iterate_simmultaneously():
 l1 = ['a', 'b', 'c']
 l2 = ['l', 'm', 's']
 for i in zip(l1, l2):
  print i
 for x, y in zip(l1, l2):
  print x + ", "+ y

def remove_duplicates_from_dictionary():
 l = {1:2, 1:2, 3:5}
 l = list(set(l.items()))
 print dict(l)

def sum_items_keys():
 l = {1:2, 1:2, 3:5}
 sum(l.keys())

def sum_items_values():
 l = {1:2, 1:2, 3:5}
 sum(l.values())

def convert_all_items_of_dictionary_to_string():
 l = {1:2, 1:2, 3:5}
 map(str, l)
if __name__ == "__main__":
 #Test any function

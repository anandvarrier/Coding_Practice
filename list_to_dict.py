#WAP to convert 2 lists to dictionary
"""
def list_to_dict():
    e_id = [1,2,3]
    e_name = ['Anand', 'Aman', 'Ramesh']
    e_salary = ['7LPA', '8LPA', '10LPA']
    e_det = list(zip(e_name,e_salary))
    result = dict(zip(e_id,e_det))
    #return result
    print(result)

res = list_to_dict()
"""
def dict_to_tuple():
    d1 = {1: ('Anand', '7LPA'), 2: ('Aman', '8LPA'), 3: ('Ramesh', '10LPA')}

    for ele in d1.items():
        print(ele)

dict_to_tuple()

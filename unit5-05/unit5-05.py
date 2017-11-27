

import ui
import random

def first_loop(arraysize1, arraysize2):
    
    list1 = []
    list2 = []
    
    
    for variable in range(arraysize1):
        randnum = random.randint(1, 50)
        list1.append(randnum)
    
    for variable2 in range(arraysize2):
        randnum2 = random.randint(1, 50)
        list2.append(randnum2)
    listOneSum = sum(list1[0:len(list1)])
    
    listtwosum = sum(list2[0:len(list2)])
    
    returnval = (list1, list2, listOneSum, listtwosum)
    
    return returnval
    	
def mainfunction(sender):
    #input
    length_of_array1 = int(view['amount_of_num_textfield'].text)
    
    length_of_array2 = int(view['number_input_textfield2'].text)
    
    array = first_loop(length_of_array1, length_of_array2)
    
    total_of_arrays = array[2] + array[3]
    
    average = total_of_arrays / (length_of_array1 + length_of_array2)
    
    view['answer_label'].text = 'your average of both lists are ' + str(average)
    


view = ui.load_view()
view.present('sheet')

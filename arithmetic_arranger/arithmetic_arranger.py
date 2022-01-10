def format_number(in_1, in_2, result):
    
    
    pad_space = 0
    
    if len(in_1) > len(in_2):
        pad_space = len(in_1)
        pass
    elif len(in_1) < len(in_2):
        pad_space = len(in_2)
        pass
    else:
        pad_space = len(in_2)
        pass
    
    formatted_in_1     = str(in_1).rjust(pad_space + 1, " ")
    formatted_in_2     = str(in_2).rjust(pad_space, " ")
    formatted_res_line = "".rjust(pad_space + 2, "-")
    formatted_result   = str(result).rjust(pad_space + 2, " ")
    # print (formatted_in_1, formatted_in_2, formatted_res_line, formatted_result) 
    return (formatted_in_1, formatted_in_2, formatted_res_line, formatted_result)
    pass

def arithmetic_arranger (input, display_res = False):
    line_1 = ""
    line_2 = ""
    line_3 = ""
    line_4 = ""
    is_error = False
    if type(input) is list:
        if len(input) > 5:
            result = "Error: Too many problems."
            is_error = True
        else:
            for i in input :
                splitted_input = i.split(' ')
                if splitted_input[1] == '+' or splitted_input[1] == '-':
                    if (len(splitted_input[0]) > 4) or (len(splitted_input[2]) > 4):
                        result = "Error: Numbers cannot be more than four digits."
                        is_error = True
                        break
                    try:
                        a = int(splitted_input[0])
                        b = int(splitted_input[2])
                    except:
                        result = "Error: Numbers must only contain digits."
                        is_error = True
                        break
                    
                    if splitted_input[1] == '+':
                        op_res = str(a + b)
                    else:
                        op_res = str(a - b)
                         
                    (num_1, num_2, res_line, op_res_f) = format_number(str(splitted_input[0]), str(splitted_input[2]) , op_res)
                    
                    line_1 = line_1 +" "+  num_1 +"    "
                    line_2 = line_2 +""+ str(splitted_input[1]) +" "+ num_2 +"    "
                    line_3 = line_3 + res_line +"    "
                    line_4 = line_4 + op_res_f +"    "                        
                else:
                    result = "Error: Operator must be '+' or '-'."
                    is_error = True
                    break
            
            if is_error == False:
                if display_res == True:
                    result = line_1.rstrip() +"\n"+ line_2.rstrip() +"\n"+ line_3.rstrip() +"\n"+ line_4.rstrip()
                else:
                    result = line_1.rstrip() +"\n"+ line_2.rstrip() +"\n"+ line_3.rstrip()
                pass
    else:
        result = False
        
    return result.rstrip()

#for my personal tests
if __name__ == '__main__': 
    # print(arithmetic_arranger(["32 - 698", "3801 - 2", "45 + 43", "123 + 49"], True))
    # print(arithmetic_arranger(["3801 - 2", "123 + 49"]))
    print(arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49']))


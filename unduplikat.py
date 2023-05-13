def eliminate_duplicates(input_list):
    output_list = []
    for i in input_list:
        if i not in output_list:
            output_list.append(i)
    return output_list

input_list = [1, 2, 3, 4, 3, 2, 1]
output_list = eliminate_duplicates(input_list)
print("Input List:", input_list)
print("Output List:", output_list)

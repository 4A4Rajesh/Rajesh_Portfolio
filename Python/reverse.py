'''

def reverse_string(string):
    new_string = list(string)
    len_str = len(new_string)
    for i in range(len_str - 1):
        new_string[i], new_string[i+1] = new_string[i+1], new_string[i]
    return " ".join(new_string)


input_string = input("Enter the input string: ")

print(f"This is the reversed string: {reverse_string(input_string)}")

join_str = ["Hello", "World"]


res_str = "-".join(join_str)

print(res_str)

'''
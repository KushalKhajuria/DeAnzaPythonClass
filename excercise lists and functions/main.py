#10.1

def nested_sum(list_of_lists):
    n_sum = 0
    for nested_list in list_of_lists:
        for number in nested_list:
            n_sum += number
    print(n_sum)

example = [[1, 2], [3], [4, 5, 6]]

nested_sum(example)

#10.2

def cumsum(list_of_nums):
    cumulative_sum_list = []
    cumulative_sum = 0
    for number in list_of_nums:
        cumulative_sum += number
        cumulative_sum_list.append(cumulative_sum)
    print(cumulative_sum_list)

example = [1, 2, 3]
cumsum(example)

#10.3

def middle(list_of_nums):
    new_list = list_of_nums[:]
    new_list.pop(0)
    new_list.pop()
    print(new_list)

example = [1, 2, 3, 4]
middle(example)

#10.4

def chop(list_of_nums):
    list_of_nums.pop(0)
    list_of_nums.pop()
    return(None)

example = [1, 2, 3, 4]
chop(example)
print(example)
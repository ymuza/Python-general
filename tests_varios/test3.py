def two_sum(nums, target):
    """Given a list of integers and a target,
       return the indices of the two numbers that add up to the target."""
    seen = {}

    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i
    return ""


def find_missing(nums):
    """Given a list of numbers from 1 to N with one number missing,
     find the missing number."""
    n = len(nums) + 1
    total = n * (n + 1) // 2
    print(n*(n+1))
    return total - sum(nums)



def flatten_list(list1):
    flat_list = []
    for item in list1:
        if isinstance(item, list):
            flat_list.extend(item)
        else:
            flat_list.append(item)
    print(flat_list)




def flatten_generator(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            # If it's a list, yield from the recursive call
            yield from flatten_generator(item)
        else:
            # If it's not a list, yield the item
            yield item



# Example usage:
my_list = [1, [2, 3], 4, [5, [6, 7, [8]], 9], 10]
flattened_generator = list(flatten_generator(my_list)) # Convert generator to list for printing
print(flattened_generator) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




#print(find_missing([1, 2, 4, 5, 6]))  # Output: 3

#print(two_sum([23, 1, 4, 55, 45, 60], 100))

print(flatten_list([[3, 2, 2], 3, 5, [6, 8, 10]]))



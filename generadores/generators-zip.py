list1 = ['.py', '.js', '.rb', '.java', '.c']
list2 = ['python', 'Javascript', 'ruby', 'java', 'c']
tupled_list = list(zip(list2, list1))  # 'zip' mergea en este caso las list1 y list2.

print(type(tupled_list))

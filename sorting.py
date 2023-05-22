def bubble_sort(my_list):
    for i in range(len(my_list)-1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp

my_list = [23, 56, 90, 20]
bubble_sort(my_list)

for i in range(len(my_list)):
     print(my_list[i])


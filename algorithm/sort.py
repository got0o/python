#数値のリストを入力として受け取り、ソート後のリストを表示する関数
nums = [9,10,8,1,4,6,2,3,5,7]

def bubble_sort(num_list,order):
    ans_list = num_list.copy()
    index = 0
    nums_len = len(ans_list)
    while(index <= (nums_len-1)):
        for i in range(index,nums_len):
            for j in range((index+1),nums_len):
                if (order == "desc"):
                    if (ans_list[i] < ans_list[j]):
                        temp = ans_list[i]
                        ans_list[i] = ans_list[j]
                        ans_list[j] = temp
                elif (order == "asc"):
                    if (ans_list[i] > ans_list[j]):
                        temp = ans_list[i]
                        ans_list[i] = ans_list[j]
                        ans_list[j] = temp
                else:
                    print("Specify asc or desc as the second argument")

        index += 1
    print(ans_list)



bubble_sort(nums,"asc")
bubble_sort(nums,"desc")
print(nums)
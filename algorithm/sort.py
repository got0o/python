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


def quick_sort(num_list,order):
    ans_list = num_list.copy()
    def quick_sort_help(nl):
        nums_len = len(nl)
        base_index = int(nums_len / 2)
        low_group = []
        high_group = []
        for n in nl:
            if(n < nl[base_index]):
                low_group.append(n)
            elif(n > nl[base_index]):
                high_group.append(n)
        if len(low_group) >= 2:
            low_group = quick_sort_help(low_group)
        if len(high_group) >= 2:
            high_group = quick_sort_help(high_group)
        if (order == "asc"):
            nl = low_group + [nl[int(nums_len/2)]] + high_group
        elif (order == "desc"):
            nl = high_group + [nl[int(nums_len/2)]] + low_group
        else:
            print("Specify asc or desc as the second argument")
        return nl
    sorted_list = quick_sort_help(ans_list)
    print(sorted_list)


quick_sort(nums,"asc")
quick_sort(nums,"desc")




#以下は作業履歴
'''

まずは元の関数を作成し、昇順、降順などを後で反映させた。
def asc_bubble_sort(num_list):
    index = 0
    nums_len = len(num_list)
    while(index <= (nums_len-1)):
        for i in range(index,nums_len):
            for j in range((index+1),nums_len):
                if (num_list[i] < num_list[j]):
                    temp = num_list[i]
                    num_list[i] = num_list[j]
                    num_list[j] = temp
        index += 1
    print(num_list)

def desc_bubble_sort(num_list):
    index = 0
    nums_len = len(num_list)
    while(index <= (nums_len-1)):
        for i in range(index,nums_len):
            for j in range((index+1),nums_len):
                if (num_list[i] > num_list[j]):
                    temp = num_list[i]
                    num_list[i] = num_list[j]
                    num_list[j] = temp
        index += 1
    print(num_list)

def quick_sort(num_list):
    def quick_sort_help(nl):
        nums_len = len(nl)
        base_index = int(nums_len / 2)
        low_group = []
        high_group = []
        for n in nl:
            if(n < nl[base_index]):
                low_group.append(n)
            elif(n > nl[base_index]):
                high_group.append(n)
        if len(low_group) >= 2:
            low_group = quick_sort_help(low_group)
        elif len(high_group) >= 2:
            high_group = quick_sort_help(high_group)
        nl = low_group + [nl[int(nums_len/2)]] + high_group
        return nl
    sorted_list = quick_sort_help(num_list)
    print(sorted_list)    

asc_bubble_sort(nums)
desc_bubble_sort(nums)
'''
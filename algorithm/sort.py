#数値のリストを入力として受け取り、ソート後のリストを表示するメソッドを持つクラスを実装
class Sort:
    def merge(self, num_list, order):
        ans_list = num_list.copy()
        def merge_sort_help(nl):
            nums_len = len(nl)
            first_nums = nl[:(nums_len//2)]
            second_nums = nl[(nums_len//2):]
            if len(first_nums) >= 2:
                first_nums = merge_sort_help(first_nums)

            if len(second_nums) >= 2:
                second_nums = merge_sort_help(second_nums)
            fs = []
            while not(first_nums==[] and second_nums==[]):
                if (first_nums == []):
                    fs.append(second_nums[0])
                    second_nums = second_nums[1:]
                elif (second_nums == []):
                    fs.append(first_nums[0])
                    first_nums = first_nums[1:]
                else:
                    if (order == "asc"):
                        if (first_nums[0] < second_nums[0]):
                            fs.append(first_nums[0])
                            first_nums = first_nums[1:]
                        elif (first_nums[0] > second_nums[0]):
                            fs.append(second_nums[0])
                            second_nums = second_nums[1:]
                    elif (order == "desc"):
                        if (first_nums[0] > second_nums[0]):
                            fs.append(first_nums[0])
                            first_nums = first_nums[1:]
                        elif (first_nums[0] < second_nums[0]):
                            fs.append(second_nums[0])
                            second_nums = second_nums[1:]
            nl = fs
            return nl
        ans_list = merge_sort_help(ans_list)
        return ans_list

    def heap(self, num_list,order):
        ans_list = num_list.copy()
        sorted_list = []
        def heap_sort_help(nl):
            while(True):
                if nl == []:
                    break
                most_i = 0
                for i in range(1,len(nl)):
                    if (order == "asc"):
                        if nl[i] < nl[most_i]:
                            most_i = i
                    elif (order == "desc"):
                        if nl[i] > nl[most_i]:
                            most_i = i
                if most_i != 0:
                    nl[0], nl[most_i] = nl[most_i], nl[0]
                nl[0], nl[len(nl)-1] = nl[len(nl)-1], nl[0]
                sorted_list.append(nl[len(nl)-1])
                nl = nl[:len(nl)-1]

            return sorted_list
        heap_sort_help(ans_list)
        return sorted_list

    def selection(self, num_list, order):
        ans_list = num_list.copy()
        nums_len = len(ans_list)

        for i in range(nums_len-1):
            selected_j = i
            for j in range((i+1),nums_len):
                if (order == "asc"):
                    if (ans_list[j] < ans_list[selected_j]):
                        selected_j = j
                if (order == "desc"):
                    if (ans_list[j] > ans_list[selected_j]):
                        selected_j = j
            if not(selected_j == i):
                temp = ans_list[i]
                ans_list[i] = ans_list[selected_j]
                ans_list[selected_j] = temp
        return ans_list

    def bubble(self, num_list, order):
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
        return ans_list

    def quick(self, num_list, order):
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
        return sorted_list

    def insertion(self, num_list, order):
        ans_list = num_list.copy()
        nums_len = len(ans_list)
        for i in range(1,nums_len):
            v = ans_list[i]
            j = i - 1
            if (order == "asc"):
                while(j>=0 and ans_list[j] > v):
                    ans_list[j+1] = ans_list[j]
                    j -= 1
            elif (order == "desc"):
                while(j>=0 and ans_list[j] < v):
                    ans_list[j+1] = ans_list[j]
                    j -= 1
            else:
                print("Specify asc or desc as the second argument")
            ans_list[j+1] = v
        return ans_list
        
test = Sort()
def test():
    nums = [9,10,8,1,4,6,2,3,5,7]
    check = Sort()
    if (check.merge(nums,"asc") == check.heap(nums,"asc") == check.selection(nums,"asc") \
         == check.bubble(nums,"asc") == check.quick(nums,"asc") == check.insertion(nums,"asc") == [1,2,3,4,5,6,7,8,9,10]):
        print("昇順ソートOK")
    if (check.merge(nums,"desc") == check.heap(nums,"desc") == check.selection(nums,"desc") \
         == check.bubble(nums,"desc") == check.quick(nums,"desc") == check.insertion(nums,"desc") == [10,9,8,7,6,5,4,3,2,1]):
        print("降順ソートOK")

#テスト用
#test()

#ソート結果を簡単に見るための一例
nums = [9,10,8,1,4,6,2,3,5,7]
x = Sort()
print(x.merge(nums,"asc"))
print(x.merge(nums,"desc"))

#以下は作業履歴やコメント
'''
・実装済み
マージソート
ヒープソート
選択ソート
バブルソート
クイックソート
挿入ソート


まずは元の関数を作成し、昇順、降順などを後で反映させた。
その後とりあえず各関数をメソッドしてクラス化し、テスト関数で簡単にソート結果をテストした。
テスト関数が柔軟でなかったり、ソートアルゴリズムの実装自体おおざっぱなので、気が向いたら改善する。

下記は実際に読みだす際の使用例
nums = [?,?,?..]
x = Sort()
x.merge(nums,"asc")
x.merge(nums,"desc")
x.heap(nums,"asc")
x.heap(nums,"desc")
x.selection(nums,"asc")
x.selection(nums,"desc")
x.bubble(nums,"asc")
x.bubble(nums,"desc")
x.quick(nums,"asc")
x.quick(nums,"desc")
x.quick(nums,"asc")
x.quick(nums,"desc")
x.insertion(nums,"asc")
x.insertion(nums,"desc")
'''
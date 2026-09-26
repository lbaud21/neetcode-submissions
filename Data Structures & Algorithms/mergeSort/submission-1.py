# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

# [0, 1, 2, 3]

# s, e = 0, 3
# m = 1

# s, e = 0, 1
# m = 0
# s, e = 2, 3
# m = 2

# s, e = 



class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.merge_sort_helper(pairs, 0, len(pairs) - 1)

    def merge_sort_helper(self, array, start, end):
        if end - start <= 0:
            return array

        m = (start + end) // 2

        self.merge_sort_helper(array, start, m)
        self.merge_sort_helper(array, m +1, end)

        self.merge(array, start, m, end)

        return array

    def merge(self, array, start, m , end):
        l = array[start:m+1]
        r = array[m+1:end+1]

        i = 0
        j = 0
        k = start

        while i < len(l) and j < len(r):
            if l[i].key <= r[j].key:
                array[k] = l[i]
                i +=1
            else:
                array[k] = r[j]
                j += 1
            k += 1

        while i < len(l):
            array[k] = l[i]
            i += 1
            k += 1

        while j < len(r):
            array[k] = r[j]
            j += 1
            k += 1

    
        

        

        

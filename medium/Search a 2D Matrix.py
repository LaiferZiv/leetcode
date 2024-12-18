class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        TRUE = -1
        FALSE = -2
        def binary_search_cols():
            l,r = 0,len(matrix)-1
            while l <= r:
                mid = (l+r)//2
                val = matrix[mid][0]
                if val == target:
                    return TRUE
                elif val < target:
                    l = mid+1
                else:
                    r = mid-1
            l,r = r,l
            if l < 0 :
                return FALSE
            return l if r < len(matrix) else len(matrix)-1
        def binary_search(arr):
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = (r + l) // 2
                val = arr[mid]
                if val == target:
                    return True
                elif val < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return False
        if not matrix:
            return False
        row = binary_search_cols()
        if row == TRUE:
            return True
        if row == FALSE:
            return False
        return binary_search(matrix[row])

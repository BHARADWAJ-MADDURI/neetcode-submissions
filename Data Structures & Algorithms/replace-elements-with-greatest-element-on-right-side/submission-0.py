class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatestele = 0
        
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[j] > greatestele:
                    greatestele = arr[j]
            arr[i] = greatestele
            greatestele = 0
        arr[len(arr) -1 ] = -1

        return arr

from typing import List

class MergeSort:

    def merge_sort(self, arr: List[int], start_index, end_index) -> List[int]:
        # base case
        if start_index == end_index:
            return arr[start_index: end_index + 1]
        # recursive case
        cutoff_index = (start_index + end_index) // 2
        first_half_sorted = self.merge_sort(arr, start_index, cutoff_index)
        second_half_sorted = self.merge_sort(arr, cutoff_index + 1, end_index)
        sorted_arr = self.merge_two_sorted_lists(first_half_sorted, second_half_sorted)
        return sorted_arr

    def merge_two_sorted_lists(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if not arr1 or not arr2:
            return arr1 + arr2

        index1, index2 = 0, 0
        merged_arr = []
        while index1 < len(arr1) and index2 < len(arr2):
            if arr1[index1] <= arr2[index2]:
                merged_arr.append(arr1[index1])
                index1 += 1
            else:
                merged_arr.append(arr2[index2])
                index2 += 1

        if index1 < len(arr1):
            merged_arr += arr1[index1:]
        if index2 < len(arr2):
            merged_arr += arr2[index2:]
        return merged_arr


# example of how to use it
if __name__ == '__main__':
    sorter = MergeSort()
    arr = [3,2,8,6,3,71,4,7,8,56,2,87,2,11,42,2,7]
    sorted_arr = sorter.merge_sort(arr, 0, len(arr)-1)
    print(sorted_arr)


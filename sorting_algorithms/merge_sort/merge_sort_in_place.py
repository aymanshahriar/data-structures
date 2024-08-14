from typing import List

class MergeSort:

    def merge_sort(self, arr: List[int], start_index: int, end_index: int) -> None:
        # base case
        if end_index - start_index < 1:
            return

        # recursive case
        cutoff_index = (start_index + end_index) // 2
        self.merge_sort(arr, start_index, cutoff_index)
        self.merge_sort(arr, cutoff_index + 1, end_index)

        self.merge_two_sorted_arrs(arr, start_index, cutoff_index, end_index)

    def merge_two_sorted_arrs(self, arr: List[int], start_index: int, cutoff_index: int, end_index: int) -> None:
        left_arr = arr[start_index: cutoff_index + 1]
        right_arr = arr[cutoff_index + 1: end_index + 1]

        index1, index2 = 0, 0
        arr_index = start_index

        while index1 < len(left_arr) and index2 < len(right_arr):
            # The = in the <= makes the algorithm stable
            if left_arr[index1] <= right_arr[index2]:
                arr[arr_index] = left_arr[index1]
                index1 += 1
            else:
                arr[arr_index] = right_arr[index2]
                index2 += 1
            arr_index += 1

        while index1 < len(left_arr):
            arr[arr_index] = left_arr[index1]
            index1 += 1
            arr_index += 1

        while index2 < len(right_arr):
            arr[arr_index] = right_arr[index2]
            index2 += 1
            arr_index += 1

# example of how to use it
if __name__ == '__main__':
    sorter = MergeSort()
    arr = [3, 2, 8, 6, 3, 71, 4, 7, 8, 56, 2, 87, 2, 11, 42, 2, 7]
    sorter.merge_sort(arr, 0, len(arr)-1)
    print(arr)
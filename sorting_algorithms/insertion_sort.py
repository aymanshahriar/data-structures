from typing import List


class InsertionSort:

    def insertion_sort(self, arr: List[int]) -> List[int]:

        # skip over the first element and iterate over every other element
        # if length of array is less than 2, then the loop will not be executed
        for i in range(1, len(arr)):
            left_index = i
            right_index = i-1

            # Keep swapping elem in left index with elem in right index as long as the elem in left index is smaller
            # than the elem in right index.
            while left_index >= 1 and arr[right_index] > arr[left_index]:
                # swap elements
                temp = arr[right_index]
                arr[right_index] = arr[left_index]
                arr[left_index] = temp

                # update left_index and right_index
                left_index -= 1
                right_index -= 1

        return arr

if __name__ == "__main__":
    sorter = InsertionSort()

    sorted = sorter.insertion_sort([3, 2, 4, 7, 3, 6, 8, 3, 3])
    print(sorted)



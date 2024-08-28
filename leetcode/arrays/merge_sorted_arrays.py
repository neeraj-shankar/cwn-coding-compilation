class MergeTwoSortedArrays:
    def __init__(self) -> None:
        pass

    @staticmethod    
    def merge_two_array_pointer(nums1, m, nums2, n):
        """
        Merge two sorted arrays nums1 and nums2 into a single sorted array in-place within nums1.

        Parameters:
        nums1 (list): The first sorted array with a length of m + n, where the first m elements are the elements to be merged,
                    and the last n elements are set to 0 and should be ignored.
        m (int): The number of elements in nums1 to be merged.
        nums2 (list): The second sorted array with a length of n.
        n (int): The number of elements in nums2.

        Returns:
        None: The function modifies nums1 in-place to contain the merged sorted array.

        Example Usage:
        >>> nums1 = [1, 2, 3, 0, 0, 0]
        >>> m = 3
        >>> nums2 = [2, 5, 6]
        >>> n = 3
        >>> merge(nums1, m, nums2, n)
        >>> print(nums1)
        [1, 2, 2, 3, 5, 6]
        """

        # Initialize pointers for nums1 and nums2
        p1 = m - 1  # Pointer for the last element in the first m elements of nums1
        p2 = n - 1  # Pointer for the last element in nums2
        p = m + n - 1  # Pointer for the last position in nums1

        # Merge nums1 and nums2 from the back to the front
        print(f"First Array status Initial:{nums1} and its length{len(nums1)}")
        print(f"Second Array Status Initial{nums2} and its length{len(nums2)}")
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            print(f"Pointer status for p1: {p1}")
            print(f"Pointer status for p2: {p2}")
            p -= 1
            print(f"Pointer status for p: {p}")
            print(f"Intermediate Status of First Array: {nums1}")

        # If there are remaining elements in nums2, copy them to nums1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1    


if __name__ == "__main__":

    first_array = [1, 2, 3, 0, 0, 0]
    first_array_size = 3
    second_array = nums2 = [2, 5, 6]
    second_array_size = 3

    MergeTwoSortedArrays.merge_two_array_pointer(first_array, first_array_size, second_array, second_array_size)
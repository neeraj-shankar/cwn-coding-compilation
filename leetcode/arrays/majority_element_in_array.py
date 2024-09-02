class MajorityElement:
    def __init__(self, arr) -> None:
        self.arr = arr

    def find_majority_element_hashmap(self):

        count_map = {}

        majority_count = len(self.arr) // 2
        for element in self.arr:
            count_map[element] = count_map.get(element, 0) + 1

            if count_map[element] > majority_count:
                return element

    def majority_element_divide_and_conquer(nums):
        def majority_element_rec(lo, hi):
            if lo == hi:
                return nums[lo]

            mid = (hi - lo) // 2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid + 1, hi)

            if left == right:
                return left

            left_count = sum(1 for i in range(lo, hi + 1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi + 1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums) - 1)
    
    def majority_element_boyer_moore(self):
        candidate = None
        count = 0

        for num in self.arr:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate


if __name__ == "__main__":

    in_arr = [2, 2, 1, 1, 1, 2, 2]

    result = MajorityElement(in_arr).find_majority_element_hashmap()
    print(result)

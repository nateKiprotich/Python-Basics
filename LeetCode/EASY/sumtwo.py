class Solution:


    def twoSum(self, nums, target):

        list_length = len(nums)
        l = []

        for i in range(list_length):
            for j in range(1, list_length):
                if nums[i] + nums[j] == target:
                    l.append(i)
                    l.append(j)
                    return l


def main():

    nums = [3, 2, 4]
    target = 6

    soln = Solution()

    lst = soln.twoSum(nums, target)

    print(lst)


if __name__ == "__main__":
    main()


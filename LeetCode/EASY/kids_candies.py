class Solution:

    def largest_number(self, candies):
        large = candies[0]

        for i in range(1, len(candies)):
            if candies[i] > large:
                large = candies[i]

        return large

    def kidsWithCandies(self, candies, extraCandies):

        large = self.largest_number(candies)
        output = []

        for i in range(len(candies)):
            if candies[i] + extraCandies >= large:
                output.append(True)
            else:
                output.append(False)

        return output


def main():
    soln = Solution()

    candies = [4, 2, 1, 1, 2]
    extraCandies = 1


    rslt = soln.kidsWithCandies(candies, extraCandies)

    print(rslt)


if __name__ == "__main__":
    main()
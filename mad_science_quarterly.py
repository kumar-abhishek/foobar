"""
Mad Science Quarterly
=====================

The deadline for submitting papers to the Mad Science Quarterly is approaching.
Professor Boolean's topic: On the Rate of Growth of Zombie Rabbits.

In the lab, Boolean's minions recorded the net growth of the number of zombits
for each day, which is the number of births minus the number of deaths (yes,
zombits do die). He realized that if these figures were to be added up over
time, it would seem like the zombits multiplied very quickly.

Then everyone shall be convinced of his mad genius! He would proudly display
these figures in his paper. Since some of the figures may be negative,
and larger numbers are more convincing, Professor Boolean will choose which
figures to show so that the sum is maximized. However, he must show a sequence
of consecutive figures without omitting the unfavorable ones - Professor Boolean
also needs to be scientific, you see.

Unfortunately, the Mad Science Quarterly limits how much data can be
shown - it is, after all, Mad. This means the mad doctor can display no more
than a certain number of figures.

Write a function answer(L, k) which returns the maximum sum Professor Boolean
can obtain by choosing some consecutive figures from his data. L will be a list
of integers representing his data, the daily net growth of the number of zombits
over a period of time. k will be the maximum number of figures he can display.

Each element of L will have absolute value no greater than 100. L will contain
at least 2 and no more than 7000 elements, and at least one element will be
positive. k will be an integer, at least 3 and no greater than the length of L.
"""


class ZombitGrowthMaximizer:
    """
    Calculates the maximum sum Professor Boolean can obtain by choosing some
    consecutive figures from his data.
    """

    @classmethod
    def calculate(cls, values, limit):
        """
        Prepares the values by removing leading and trailing negatives,
        checks for special cases, and delegates the final calculation.
        """

        # get a copy of the values without leading and trailing negatives
        _values = cls.trim(values)

        # if no values are left over, it means that they were all negative,
        # in which case all we want to do is return the maximum value
        # of the original values, ie. greatest of the negatives.
        if not _values:
            return max(values)

        # get and return the maximal sum of the values given the limit
        return cls.maximal(_values, limit)

    @classmethod
    def maximal(cls, values, limit):
        """
        Calculates the maximum growth metric that can be obtained from
        a given set of values, given a limit on how many consecutive
        numbers are allowed to be used.
        """

        # used to store the maximum sum during the iteration,
        # and will always be non-negative.
        maximum = 0

        # step through each value from back to front
        for i in xrange(len(values) - 1, 0, -1):

            # initialize the index for the secondary loop
            j = i

            # an accumulator to keep track of the current sum
            acc = 0

            # the number of values that have been added to the accumulator
            count = 0

            # keep looping as long as there are numbers ahead,
            # and if we haven't reached the limit yet
            while j >= 0 and count < limit:

                if values[j] >= 0:

                    # a positive value can be added to the accumulator
                    acc += values[j]
                    count += 1

                    # update the maximum if the accumulator is greater
                    maximum = max(maximum, acc)

                else:
                    # a negative value

                    # an accumulator for collecting negative values
                    nacc = values[j]
                    ncount = 1

                    # accumulate any successive negative values
                    while values[j - 1] < 0:
                        nacc += values[j - 1]
                        ncount += 1
                        j -= 1

                    # if the sum of the negative accumulator doesn't
                    # negate the positive accumulator and the number
                    # of values that contributed to the negative sum
                    # doesn't break the limit, update the positive
                    # accumulator with the negative sum
                    if acc + nacc > 0 and count + ncount < limit:
                        count += ncount
                        acc += nacc
                    else:
                        # either a run of negatives broke past the limit,
                        # or the negative sum was too large.
                        break

                # continue on to the next index
                j -= 1

        return maximum

    @classmethod
    def trim(cls, values):
        """
        Removes leading and trailing negative values from a list
        """

        length = len(values)

        i = 0
        j = 1

        # count the number of leading negatives
        while i < length and values[i] < 0:
            i += 1

        # count the number of trailing negatives
        while j <= length and values[-j] < 0:
            j += 1

        # slice the values to exclude the leading and trailing negatives
        _values = values[i:length - j + 1]

        return _values


def answer(L, k):
    return ZombitGrowthMaximizer.calculate(L, k)
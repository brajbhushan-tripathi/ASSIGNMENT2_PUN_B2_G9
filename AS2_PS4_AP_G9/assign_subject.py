class AssignSubject:
    def count_allocations(self, prefrences):
        # maximum number of possible subsets
        msub = 2 ** 11
        allocation = [0] * msub
        allocation[msub-1] = 1
        # proceed in bottom up manner
        for mask in range(msub-1, -1, -1):
            # now find the student
            j = mask
            student = 0

            # count no. of set bits in mask
            while j:
                student += (j & 1)
                j = int(j/2)

            # so, this is a state for student
            for i in range(11):
                if(prefrences[student-1][i] and not(mask & (1 << i))):
                    allocation[mask] += allocation[mask | (1 << i)]

        # returning the result
        return allocation[0]

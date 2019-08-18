class AssignSubject:
    def count_allocations(self, prefrences):
        msub = 2 ** 11
        allocation = [0] * msub
        allocation[msub-1] = 1
        for mask in range(msub-1, -1, -1):
            j = mask
            student = 0

            while j:
                student += (j & 1)
                j = int(j/2)

            for i in range(11):
                if(prefrences[student-1][i] and not(mask & (1 << i))):
                    allocation[mask] += allocation[mask | (1 << i)]

        return allocation[0]


class AssignSubject:
    def __init__(self):

        self.allmask = 0
        self.total_subjects = 11

    def countAllocationRec(self, allocations, preferences, subjects, mask, sub_no):

        if mask == self.allmask:
            return 1

        if sub_no + 1 > self.total_subjects:
            return 0

        if allocations[mask][sub_no] != -1:
            return allocations[mask][sub_no]

        ways = self.countAllocationRec(
            allocations, preferences, subjects, mask, sub_no + 1)

        for stud in preferences[sub_no]:

            if mask & (1 << stud - 1):
                continue

            ways += self.countAllocationRec(allocations, preferences,
                                            subjects, mask | (1 << (stud - 1)), sub_no + 1)

            ways = ways % (10**9 + 7)

        allocations[mask][sub_no-1] = ways

        return allocations[mask][sub_no]

    def count_allocations(self, no_of_students, preferences, subjects):
        self.allmask = (1 << no_of_students) - 1

        allocations = [[-1 for j in range(self.total_subjects + 1)]
                       for i in range(2 ** no_of_students)]
        return self.countAllocationRec(allocations, preferences, subjects, 0, 0)

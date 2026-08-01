# Last updated: 1/8/2026, 5:22:59 p.m.
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        aux = []

        while students:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                students += aux
                aux = []
            else:
                aux.append(students.pop(0))

        return len(sandwiches)
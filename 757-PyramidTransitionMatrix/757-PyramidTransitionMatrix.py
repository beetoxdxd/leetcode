# Last updated: 1/8/2026, 5:25:59 p.m.
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        possibilities = defaultdict(list)
        for pyramid in allowed:
            possibilities[pyramid[:2]].append(pyramid[2])

        memo = {}

        def construction(bottom: str, above: str) -> bool:
            state = (bottom, above)
            if state in memo: return memo[state]

            if len(bottom) == 1: return True
            if len(above) == len(bottom) - 1: return construction(above, "")
            i = len(above)
            if bottom[i:i+2] not in possibilities: 
                memo[state] = False
                return False

            for option in possibilities[bottom[i:i+2]]:
                if construction(bottom, above + option): 
                    memo[state] = True
                    return True

            memo[state] = False
            return False

        return construction(bottom, "")

# Last updated: 22/7/2026, 11:35:44 p.m.
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        zipped = zip(positions, healths, directions)        
        sorted_trip = sorted(zipped)       
        stack = []

        for current in sorted_trip:
            aux = current

            while stack and stack[-1][2] == 'R' and aux[2] == 'L':
                if aux[1] > stack[-1][1]: 
                    stack.pop()
                    aux = (aux[0], aux[1]-1, aux[2])
                elif aux[1] < stack[-1][1]: 
                    stack[-1] = (stack[-1][0], stack[-1][1]-1, stack[-1][2])
                    aux = None; break
                else: 
                    stack.pop()
                    aux = None; break

            if aux: stack.append(aux)

        ans = []
        index = defaultdict(int)
        for i in range(len(stack)):
            trip = stack[i]
            index[trip[0]] = i

        for pos in positions:
            if pos in index: 
                ans.append(stack[index[pos]][1])

        return ans
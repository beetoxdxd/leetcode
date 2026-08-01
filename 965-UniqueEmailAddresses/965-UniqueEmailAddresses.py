# Last updated: 1/8/2026, 5:25:27 p.m.
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        different = defaultdict(bool)
        
        for email in emails:
            local, domain = email.split('@')
            
            aux = ""
            for char in local:
                if char == ".": continue
                if char == "+": break
                aux += char
            aux += '@' + domain
            
            different[aux] = True
        
        k = list(different.keys())
        return len(k)
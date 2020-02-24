class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        for i in emails:
            domain = i.split('@')[1]
            local = ''.join(i.split('@')[0].split('+')[0].split('.'))
            ans.add(local+'@'+domain)
        return len(ans)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #mapping Char count to list of Anagrams
        #[1e, 1a, 1t] => ['ate', 'eat', 'tea']
        res = defaultdict(list)

        for s in strs:
           sortedS = ''.join(sorted(s))
           res[sortedS].append(s)
        
        return list(res.values())
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        clist = list(Counter(nums).items())
        l = len(clist)
        self.quickSelection(clist, 0, l - 1, k)
        return [clist[i][0] for i in range(l-1, l-k-1, -1)]
        
    def quickSelection(self, clist: List, bg: int, ed: int, k: int) -> None:
        if bg < ed:
            pivot = self.sortList(clist, bg, ed)
            # make sure the right part of the array is well-sorted
            self.quickSelection(clist, pivot+1, ed, k)
            k -= (ed - pivot + 1)
            if k > 0:
                self.quickSelection(clist, bg, pivot, k)
            
    def sortList(self, clist: List, bg: int, ed: int) -> int:
        pivot_value = clist[bg]
        i = bg
        j = ed
        while i < j:
            # from ending to begining
            while i < j and clist[j][1] >= pivot_value[1]:
                j -= 1
            if i < j:
                clist[i] = clist[j]
                i += 1
            while i < j and clist[i][1] < pivot_value[1]:
                i += 1
            if i < j:
                clist[j] = clist[i]
        # i == j in this time
        clist[i] = pivot_value
        return i

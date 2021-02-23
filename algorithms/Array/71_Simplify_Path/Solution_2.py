class Solution:
    def simplifyPath(self, path: str) -> str:
        eles = list()
        for ele in path.split('/'):
            if ele == "..":
                if eles:
                    eles.pop()
            elif ele and ele != ".":
                eles.append(ele)
        
        return "/" + "/".join(eles)

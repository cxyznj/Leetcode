class Solution:
    def simplifyPath(self, path: str) -> str:
        eles = list()
        ele = None
        for i in range(len(path)):
            if path[i] == '/':
                # add a file/directory name, or process "." ".."
                if ele:
                    if ele == ".":
                        pass
                    elif ele == "..":
                        if eles:
                            eles.pop()
                    else:
                        eles.append(ele)
                    ele = None
                
                # throw repeated slash
                while i+1 < len(path) and path[i+1] == '/':
                    i += 1
            else:
                if not ele:
                    ele = path[i]
                else:
                    ele += path[i]
        # ending process
        if ele:
            if ele == ".":
                pass
            elif ele == "..":
                if eles:
                    eles.pop()
            else:
                eles.append(ele)
        
        canpath = "/" + "/".join(eles)
        
        return canpath

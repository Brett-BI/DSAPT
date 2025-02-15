class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        # iterate over a list
        for p in path.split("/"):
            if p == "..": # up one directory
                if stack:
                    stack.pop()
            elif p == "." or not p: # current directory or nothing
                continue
            else: # otherwise append for the .join() later
                stack.append(p)
                
        # join everything from the stack with "/" as the delimiter
        final_path = "/" + "/".join(stack)

        return final_path
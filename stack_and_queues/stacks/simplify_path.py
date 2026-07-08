# Approach 1: Raw SOlution


class Solution:
    def simplifyPath(self, path: str) -> str:

        stack = []

        curr = ""
        stack = []
        path += "/"

        for ch in path:
            if ch == "/":
                if curr:
                    if curr == "..":
                        if stack:
                            stack.pop()
                    elif curr != ".":
                        stack.append(curr)
                curr = ""
            else:
                curr += ch

        return "/" + "/".join(stack)


# Approach 2
class Solution2:
    def simplifyPath(self, path: str) -> str:

        # Initialize a stack
        stack = []

        # Split the input string on "/" as the delimiter
        # and process each portion one by one
        for portion in path.split("/"):
            # If the current component is a "..", then
            # we pop an entry from the stack if it's non-empty
            if portion == "..":
                if stack:
                    stack.pop()
            elif portion == "." or not portion:
                # A no-op for a "." or an empty string
                continue
            else:
                # Finally, a legitimate directory name, so we add it
                # to our stack
                stack.append(portion)

        # Stich together all the directory names together
        final_str = "/" + "/".join(stack)
        return final_str

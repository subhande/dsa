# https://leetcode.com/discuss/post/5563819/google-onsite-l4-by-anonymous_user-a0uh/
"""
You need to design function which will resolve the given string by replacing the variables with their values. The variable will be enclosed in specific delimiter.
For eg b -> #a#src
a -> data#c#
c -> base
If input is hello#b# output should be -> hellodatabasesrc.
The variable name wont contain delimiter
similar to:
https://leetcode.com/discuss/interview-experience/1670275/imp-facebook-e45-london
"""
from collections import defaultdict, deque
def replace_variable(string: str, variables: dict) -> str:
    """
    Replaces variables in the string with their corresponding values from the variables dictionary.

    Args:
        string (str): The input string containing variables.
        variables (dict): A dictionary mapping variable names to their values.

    Returns:
        str: The string with variables replaced by their values.
    """

    # Build the graph for depecendency resolution
    graph = defaultdict(list)
    for key, value in variables.items():
        idx = 0
        while idx < len(value):
            if value[idx] == '#':
                right = idx + 1
                while right < len(value) and value[right] != '#':
                    right += 1
                graph[key].append(value[idx+1:right])
                idx = right + 1
            else:
                idx += 1

    # Topological sort to resolve dependencies

    inDegree = defaultdict(int)
    for key in graph:
        for node in graph[key]:
            inDegree[node] += 1

    # 0 in-degree nodes
    queue = deque()
    for k in graph.keys():
        if inDegree[k] == 0:
            queue.append(k)

    topoOrder = []
    while queue:
        node = queue.popleft()
        topoOrder.append(node)

        for neighbor in graph[node]:
            inDegree[neighbor] -= 1
            if inDegree[neighbor] == 0:
                queue.append(neighbor)

    print("Topological Order:", topoOrder)

    for node in topoOrder:
        if node in variables:
            string = string.replace(f"#{node}#", variables[node])

    return string



# Example usage
if __name__ == "__main__":
    input_string = "hello#b#"
    variables_dict = {
        'b': '#a#src',
        'a': 'data#c#',
        'c': 'base'
    }
    result = replace_variable(input_string, variables_dict)
    print(result)  # Output: hellodatabasesrc

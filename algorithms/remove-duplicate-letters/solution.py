
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = {}

        # Step 1: Store the last occurrence of each character
        for i, c in enumerate(s):
            last_index[c] = i

        stack = []
        visited = set()

        # Step 2: Process each character
        for i, c in enumerate(s):

            # Skip if character is already present
            if c in visited:
                continue

            # Step 3: Remove larger characters if they occur again later
            while (stack and stack[-1] > c
                   and last_index[stack[-1]] > i):

                removed = stack.pop()
                visited.remove(removed)

            # Step 4: Add current character
            stack.append(c)
            visited.add(c)

        return ''.join(stack)

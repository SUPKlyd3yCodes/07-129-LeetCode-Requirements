class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxarea = 0
        tempW = 0
        heights.append(-1)
        for index,height in enumerate(heights):
            while stack and height < heights[stack[-1]]:
                prevI = stack.pop()
                prevH = heights[prevI]
                if stack:
                    tempW = index - stack[-1] - 1
                else:
                    tempW = index
                maxarea = max(maxarea,prevH*tempW)

            stack.append(index)
        return maxarea

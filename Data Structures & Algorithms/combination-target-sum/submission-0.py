class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        length = len(candidates)

        def dfs(ind, currList, currSum):
            if ind >= length or currSum > target:
                return

            if currSum == target:
                res.append(currList.copy())
                return

            dfs(ind, currList + [candidates[ind]], currSum + candidates[ind])
            dfs(ind + 1, currList, currSum)

        dfs(0, [], 0)

        return res


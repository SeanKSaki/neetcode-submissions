class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        candidates = {}
        for num in nums:
            if num in candidates:
                candidates[num] += 1
            else:
                candidates[num] = 1
        results = []
        for _ in range(k):
            results.append(max(candidates, key=candidates.get))
            candidates.pop(max(candidates, key=candidates.get))
        return results
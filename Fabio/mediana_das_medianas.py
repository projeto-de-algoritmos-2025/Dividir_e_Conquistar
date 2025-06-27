class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def select(arr, k):
            # Base case: se pequeno, ordena e retorna o k-ésimo
            if len(arr) <= 5:
                return sorted(arr)[k]

            # Divide arr em grupos de 5 e calcula as medianas
            medians = []
            for i in range(0, len(arr), 5):
                group = arr[i:i+5]
                medians.append(sorted(group)[len(group)//2])

            # Recursivamente encontra a mediana das medianas
            pivot = select(medians, len(medians)//2)

            # Particiona o array em 3 partes: < pivot, == pivot, > pivot
            lows = [el for el in arr if el < pivot]
            highs = [el for el in arr if el > pivot]
            pivots = [el for el in arr if el == pivot]

            # Decide em qual parte o k-ésimo está
            if k < len(lows):
                return select(lows, k)
            elif k < len(lows) + len(pivots):
                return pivot
            else:
                return select(highs, k - len(lows) - len(pivots))

        n = len(nums)
        # O k-ésimo maior é o (n-k)-ésimo menor
        return select(nums, n - k)

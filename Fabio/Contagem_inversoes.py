class Solution(object):
    def numberOfPermutations(self, n, requirements):
        """
        :type n: int
        :type requirements: List[List[int]]
        :rtype: int
        """
        MOD = 10**9 + 7

        # Map endi to cnti for quick lookup
        req = dict(requirements)

        # dp[i][k]: number of ways to arrange first i numbers with k inversions
        max_inv = 400
        dp = [[0] * (max_inv + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            # prefix sum for optimization
            prefix = [0] * (max_inv + 2)
            for k in range(max_inv + 1):
                prefix[k + 1] = (prefix[k] + dp[i - 1][k]) % MOD
            for k in range(max_inv + 1):
                # When adding the i-th number, it can create up to i-1 new inversions
                if k <= (i - 1) * i // 2:
                    left = max(0, k - (i - 1))
                    right = k
                    dp[i][k] = (prefix[right + 1] - prefix[left]) % MOD

            # If there's a requirement for this prefix, zero out invalid inversion counts
            if (i - 1) in req:
                cnt = req[i - 1]
                for k in range(max_inv + 1):
                    if k != cnt:
                        dp[i][k] = 0

        # The answer is the sum of valid permutations for the full array
        return sum(dp[n]) % MOD

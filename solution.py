MOD = 10**9 + 7

M = int(input())

dp = [0] * (M + 1)
if M >= 0:
    dp[0] = 0
if M >= 1:
    dp[1] = 1
if M >= 2:
    dp[2] = 2

for n in range(3, M + 1):
    dp[n] = (dp[n-1] + dp[n-2] + dp[n-3] + 1) % MOD

result = [str(dp[i]) for i in range(1, M + 1)]
print(' '.join(result))

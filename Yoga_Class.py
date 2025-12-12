t = int(input())
for _ in range(t):
    n, x, y = map(int, input().split())
    two_hour_profit = max(2*x, y)
    max_money = (n // 2) * two_hour_profit + (n % 2) * x
    print(max_money)


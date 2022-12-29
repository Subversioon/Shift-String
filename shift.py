def get_cost( src: str, dst: str):
    ans = 0
    n = len(src)
    for i in range(n):
        ca = ord(src[i])
        cb = ord(dst[i])
        cost = (cb-ca+26)%26
        ans = ans + min( cost, 26-cost)
    return ans
 
if __name__ == '__main__':
    
    n = int(input().strip())
    s = input().strip()
    m = int(input().strip())
    arr = [s]
    for i in range(m):
        arr.append(input().strip())
    m = m + 1
    M = 2**m
 
    # print(arr)
    
    q = []
    dp = [[ -1 for j in range(m)] for i in range(M)]
    cost = [[0 for j in range(m)] for i in range(m)]
    
    dp[1][0] = 0
    q.append((1,0))
    
    for i in range(m):
        for j in range(m):
            cost[i][j] = get_cost( arr[i], arr[j])
    
    while len(q) > 0:
        p = q[0]
        q.pop(0)
        mask = p[0]
        last = p[1]
        for i in range(m):
            if (mask&(1<<i))==0:
                if dp[mask^(1<<i)][i]==-1:
                    q.append((mask^(1<<i), i))
                    dp[mask^(1<<i)][i] = 1000000
                dp[mask^(1<<i)][i] = min( dp[mask^(1<<i)][i], cost[last][i]+dp[mask][last])
        
    ans = 1000000
    for last in range(m):
        if dp[M-1][last]==-1:
            continue
        ans = min( ans, dp[M-1][last])
    
    print(ans)

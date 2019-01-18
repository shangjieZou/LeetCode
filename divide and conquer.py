# divide and conquer
def kClosest(points, K):
    import math
    import random
    distance = lambda i: math.sqrt(points[i][0]**2 + points[i][1])

    def work(i, j, K):
        if i >= j: return
        oi, oj = i, j
        pivot = distance(random.randint(i, j))  # 生成的随机数n：i<=n<=j

        # 这一块把最大的数放在最后---------------------------
        while i < j:
            if distance(i) < pivot:
                i += 1
            if distance(j) > pivot:
                j -= 1
            points[i], points[j] = points[j], points[i]
        # -----------------------------------------------------

        if K <= i - oi + 1:
            work(oi, i, K)
        else:
            work(i + 1, oj, K - (i - oi + 1))

    work(0, len(points) - 1, K)
    return points[:K]

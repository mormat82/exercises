#moje na 50%

# def solution(A):
#     n = 0
#     sol = []
#     while n < (len(A)-1):
#         dif = abs(sum(A[0:n+1])-sum(A[n+1:]))
#         n += 1
#         sol.append(dif)
#     return min(sol)


# to na 100%

def solution(A):
    left = A[0]
    right = sum(A[1:])
    min_dif = abs(left - right)

    for index in range(1, len(A)-1):
        left += A[index]
        right -= A[index]
        if abs(left-right) < min_dif:
            min_dif = abs(left-right)

    return min_dif



print(solution([3, 1, 2, 4, 3]))


# moje pierwsze rozwiązanie na 50%
#
# def solution(A):
#     B = sorted(A)
#     n = 0
#     for number in B:
#         if B[n] == n + 1:
#             n += 1
#         else:
#             return number - 1


# drugie rozwiązanie na 100%
def solution(A):
    B = sorted(A)
    if A==[]:
        return 1
    elif B[0]==2:
        return 1
    elif B[-1] == len(B):
        return len(B) + 1
    else:
        for n in range(1, len(A)):
            if B[n] - B[n-1] > 1 and B[-1] == len(A)+1:
                mis_el = B[n]-1
                return mis_el



print(solution([1]))
print(solution([2]))
print(solution([]))
print(solution([2,3]))
print(solution([1,2]))
print(solution([2, 3, 1, 4]))
print(solution([4, 3, 1, 5]))
print(solution([4, 3, 1, 5, 2, 7, 8]))
print(solution([4, 3, 6, 5, 2, 7, 8]))


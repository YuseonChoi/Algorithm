""" <좋다> https://www.acmicpc.net/problem/1253 """

def solve():
    cnt = 0
    nums.sort()
    for i in range(len(nums)):
        if search(i, nums[i]):
            cnt += 1
    print(cnt)

def search(i, target):
    temp = nums[:i] + nums[i+1:]  # 타겟이 되는 nums[i]를 제외하고 탐색
    left = 0
    right = n-2  # 마지막 인덱스 n-1에서 타겟값 하나 더 빼서 n-2
    while left < right:
        sum = temp[left] + temp[right]
        if target < sum:
            right -= 1
        elif target > sum:
            left += 1
        else:
            return True
    return False


import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
solve()


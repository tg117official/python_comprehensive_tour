from .basic import add  # relative import within the package

def mean(nums):
    total = 0
    for n in nums:
        total = add(total, n)
    return total / len(nums) if nums else 0

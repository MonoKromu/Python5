def same_by(characteristic, objects):
    result = [characteristic(i) for i in objects]
    return all(result) or not any(result)


nums = [10, 25, 40, 50]
print(same_by(lambda x: x / 10 > 5, nums))
print(same_by(lambda x: x % 2, nums))

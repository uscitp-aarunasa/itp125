n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here

def flatten(lists):
    results = []
    for i in lists:
        for number in i:
            results.append(number)
    return results

print flatten(n)

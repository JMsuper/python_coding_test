import itertools

# 재귀함수를 이용한 순열
def permutation(arr,r):
    result = []
    if r > len(arr):
        return result
    if r == 1:
        for i in arr:
            result.append([i])
    elif r > 1:
        for i in range(len(arr)):
            ans = [j for j in arr]
            ans.remove(arr[i])
            for permuted in permutation(ans,r-1):
                result.append([arr[i]] + permuted)
    return result

# 재귀함수를 이용한 중복순열
def permutation_with_repetition(arr,r): 
    result = []
    if r == 1:
        for i in arr:
            result.append([i])
    elif r > 1:
        for item in arr:
            for permuted in permutation_with_repetition(arr,r-1):
                result.append([item] + permuted)
    return result     

def combination(arr,r):
    result = []
    if r == 1:
        for i in arr:
            result.append([i])
    if r > 1:
        for i in range(len(arr)):
            for item in combination(arr[i+1:],r-1):
                result.append([arr[i]] + item)
    return result

def combination_with_repetition(arr,r):
    result = []
    if r == 1:
        for i in arr:
            result.append([i])
    if r > 1:
        for i in range(len(arr)):
            for item in combination(arr[i:],r-1):
                result.append([arr[i]] + item)
    return result

def main():
    # print(permutation([1,2,3,4],2))
    # print()
    # for item in itertools.permutations([1,2,3,4],2):
    #     print(item,end=" ")

    # print(permutation_with_repetition([1,2,3],3))
    # for item in itertools.product([1,2,3], repeat=3):
    #     print(item,end=" ")  
    # print(combination([1,2,3,4],2))
    # for item in itertools.combinations([1,2,3,4],2):
    #     print(item,end=" ")
    print(combination_with_repetition([1,2,3],2))
    for item in itertools.combinations_with_replacement([1,2,3],2):
        print(item,end=" ")

if __name__ == "__main__":
    main()
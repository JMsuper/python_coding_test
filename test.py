import bisect

def main():
    test_l = [0,2,4,5,6,7,8,9]
    print(bisect.bisect_left(test_l,6))

if __name__ == "__main__":
    main()
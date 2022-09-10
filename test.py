import bisect

def main():
    test_l = [5,6,7,8,9]
    print(bisect.bisect_left(test_l,9))

if __name__ == "__main__":
    main()
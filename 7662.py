import sys
import heapq

input = sys.stdin.readline
print = sys.stdout.write

def main():
    t = int(input().rstrip())
    for _ in range(t):
        k = int(input().rstrip())
        max_heap = []
        min_heap = []
        item_dict = {}
        item_cnt = 0
        for i in range(k):
            cmd, val = input().rstrip().split()
            val = int(val)
            if cmd == "I":
                item_cnt += 1
                heapq.heappush(max_heap,-val)
                heapq.heappush(min_heap,val)
                if val in item_dict:
                    item_dict[val] += 1
                else:
                    item_dict[val] = 1
            else:
                if item_cnt > 0:
                    item_cnt -= 1
                if val == 1:
                    if len(max_heap) > 0:
                        while max_heap:
                            max_pop = -heapq.heappop(max_heap)
                            if item_dict[max_pop] > 0:
                                item_dict[max_pop] -= 1
                                break
                            else:
                                continue
                else:
                    if len(min_heap) > 0:
                        while min_heap:
                            min_pop = heapq.heappop(min_heap)
                            if item_dict[min_pop] > 0:
                                item_dict[min_pop] -= 1
                                break
                            else:
                                continue
        if item_cnt == 0:
            print("EMPTY\n")
        else:
            max_val = 0
            min_val = 0
            while max_heap:
                max_pop = -heapq.heappop(max_heap)
                if item_dict[max_pop] > 0:
                    max_val = max_pop
                    break
            while min_heap:
                min_pop = heapq.heappop(min_heap)
                if item_dict[min_pop] > 0:
                    min_val = min_pop
                    break
            print(str(max_val) + " " + str(min_val) + "\n")

if __name__ == "__main__":
    main()
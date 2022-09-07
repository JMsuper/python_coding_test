import heapq

def main():
    queue = []
    heapq.heappush(queue,[1,5])
    heapq.heappush(queue,[2,6])
    heapq.heappush(queue,[2,4,2])
    heapq.heappush(queue,[2,4,1])
    
    while queue:
        print(heapq.heappop(queue))

if __name__ == "__main__":
    main()
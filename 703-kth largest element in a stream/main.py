from queue import PriorityQueue as PQ


class KthLargest:
    def __init__(self, k, nums):
        self.pq = PQ()
        self.k = k
        for num in nums:
            self.pq.put(num)
            if self.pq.qsize() > self.k:
                self.pq.get()

    def add(self, val):
        self.pq.put(val)
        if self.pq.qsize() > self.k:
            self.pq.get()

        res = self.pq.get()
        self.pq.put(res)
        return res


#k = 3
#arr = [4, 5, 8, 2]

#kthLargest = KthLargest(k, arr)
#print(kthLargest.add(3))
#print(kthLargest.add(5))
#print(kthLargest.add(10))
#print(kthLargest.add(9))
#print(kthLargest.add(4))

k = 1
arr = []

kthLargest = KthLargest(k, arr)
print(kthLargest.add(-3))
print(kthLargest.add(-2))
print(kthLargest.add(-4))
print(kthLargest.add(0))
print(kthLargest.add(4))

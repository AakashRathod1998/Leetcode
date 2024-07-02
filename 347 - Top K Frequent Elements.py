class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = collections.Counter(nums)
        min_heap = []

        for num, freq in counts.items():
            heapq.heappush(min_heap,(freq, num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [i[1] for i in min_heap]


        # frequency_map = Counter(nums)
        
        # # Step 2: Build the min-heap with only the k most frequent elements
        # heap = []
        # for num, freq in frequency_map.items():
        #     # Use a tuple of (freq, num) for the min-heap
        #     heapq.heappush(heap, (freq, num))
        #     print(heap)
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        
        # # Step 3: Extract the elements from the heap
        # top_k_elements = [heapq.heappop(heap)[1] for _ in range(len(heap))]
        # return top_k_elements[::-1]  # Reverse to get highest to lowest if needed

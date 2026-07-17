class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num] = 1

        freq_arr = [[] for i in range(len(nums))]
        for key in freq.keys():
            freq_arr[freq[key]-1].append(key)
        most_freq = []
        for i in range(len(nums)-1, -1, -1):
            if freq_arr[i]:
                if len(most_freq)<k:
                    most_freq+=freq_arr[i]
                else:
                    break
        return most_freq if len(most_freq)<=k else most_freq[:k]
        



        
from typing import List
# https://leetcode.com/problems/rearranging-fruits/

class Solution(object):
    def minCost(self, basket1: List[int], basket2: List[int]):
        """
        :type basket1: List[int]
        :type basket2: List[int]
        :rtype: int
        """
        dict1 = {}
        dict2 = {}
        sumdict = {}
        n = len(basket1) # le lunghezze sono uguali
        for i in range(n):
            dict1[basket1[i]] = dict1.get(basket1[i],0) + 1
            dict2[basket2[i]] = dict2.get(basket2[i],0) + 1
            sumdict[basket1[i]] = sumdict.get(basket1[i],0) + 1
            sumdict[basket2[i]] = sumdict.get(basket2[i],0) + 1
        for key in sumdict:
            if sumdict[key] % 2 != 0:
                return -1 # le frequenze non sono pari quindi è inutile provare a scambiare
        # devo trovare i primi due elementi nelle due collezioni con frequenze diverse
        possible_swap_bucket_1 = -1
        possible_swap_bucket_2 = -1
        cost = 0
        finish = False
        max_iter = n * 2  # sicurezza: massimo 2n iterazioni
        iter_count = 0
        min_fruit = min(list(dict1.keys()) + list(dict2.keys()))
        while not finish and iter_count < max_iter:
            iter_count += 1
            found1 = False
            found2 = False
            for i in range(n):
                if basket1[i] not in dict2 or dict1[basket1[i]] > dict2.get(basket1[i], 0):
                    possible_swap_bucket_1 = basket1[i]
                    found1 = True
                    break
            for i in range(n):
                if basket2[i] not in dict1 or dict2[basket2[i]] > dict1.get(basket2[i], 0):
                    possible_swap_bucket_2 = basket2[i]
                    found2 = True
                    break
            if not found1 and not found2:
                finish = True
                break
            # swap solo se entrambi trovati e le frequenze sono ancora sbilanciate
            while found1 and found2 and dict1.get(possible_swap_bucket_1,0) > dict2.get(possible_swap_bucket_1,0) and dict2.get(possible_swap_bucket_2,0) > dict1.get(possible_swap_bucket_2,0):
                dict1[possible_swap_bucket_1] -= 1
                dict2[possible_swap_bucket_1] = dict2.get(possible_swap_bucket_1, 0) + 1
                dict2[possible_swap_bucket_2] -= 1
                dict1[possible_swap_bucket_2] = dict1.get(possible_swap_bucket_2, 0) + 1
                cost += min(min(possible_swap_bucket_1, possible_swap_bucket_2), 2 * min_fruit)
        # se non sono riuscito a pareggiare, ritorno -1
        for key in dict1:
            if dict1[key] != dict2.get(key,0):
                return -1
        return cost

if __name__ == "__main__":
    sol = Solution()
    # Example 1
    basket1 = [4,2,2,2]
    basket2 = [1,4,1,2]
    print("Output Example 1:", sol.minCost(basket1, basket2))  # Expected: 1

    # Example 2
    basket1 = [2,3,4,1]
    basket2 = [3,2,5,1]
    print("Output Example 2:", sol.minCost(basket1, basket2))  # Expected: -1

    basket1 = [4,4,4,4,3]
    basket2 = [5,5,5,5,3]
    print("Output Custom Test:", sol.minCost(basket1, basket2))  # Expected: -1
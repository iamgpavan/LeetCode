class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        next_slot = {"0":"1", "1":"2", "2":"3", "3":"4", "4":"5", "5":"6", "6":"7", "7":"8", "8":"9", "9":"0"}
        prev_slot = {"0":"9", "1":"0", "2":"1", "3":"2", "4":"3", "5":"4", "6":"5", "7":"6", "8":"7", "9":"8"}
        
        visited_comb = set(deadends)
        pending_comb = deque()
        
        turns = 0
        
        if '0000' in visited_comb:
            return -1
        
        pending_comb.append("0000")
        visited_comb.add("0000")
        
        while pending_comb:
            curr_level = len(pending_comb)
            for _ in range(curr_level):
                curr_comb = pending_comb.popleft()
                
                if curr_comb == target:
                    return turns
                
                for i in range(4):
                    new_comb = list(curr_comb)
                    new_comb[i] = next_slot[new_comb[i]]
                    new_comb_str = "".join(new_comb)
                    
                    if new_comb_str not in visited_comb:
                        visited_comb.add(new_comb_str)
                        pending_comb.append(new_comb_str)
                        
                    new_comb = list(curr_comb)
                    new_comb[i] = prev_slot[new_comb[i]]
                    new_comb_str = "".join(new_comb)
                    
                    if new_comb_str not in visited_comb:
                        visited_comb.add(new_comb_str)
                        pending_comb.append(new_comb_str)
                
            turns += 1
        
        return -1
                        
                        
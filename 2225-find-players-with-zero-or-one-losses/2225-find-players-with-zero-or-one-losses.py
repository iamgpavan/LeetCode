class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        looser_map = {}
        
        for match in matches:
            winner = match[0]
            looser = match[1]
            
            looser_map[winner] = looser_map.get(winner, 0)
            
            looser_map[looser] = looser_map.get(looser, 0) + 1
        
        no_match_loss = []
        one_match_loss = []
        
        for player in looser_map:
            if(looser_map[player] == 0):
                no_match_loss.append(player)
            if(looser_map[player] == 1):
                one_match_loss.append(player)
        
        no_match_loss.sort()
        one_match_loss.sort()
        
        return [no_match_loss, one_match_loss]
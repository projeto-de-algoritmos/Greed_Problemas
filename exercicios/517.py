class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        num_machines = len(machines)
        total_dresses = sum(machines)
        
        if total_dresses % num_machines != 0:
            return -1
        
        target_dresses = total_dresses // num_machines
        min_moves = 0
        dresses_so_far = 0
        
        for i in range(num_machines):
            dresses_so_far += machines[i] - target_dresses
            min_moves = max(min_moves, abs(dresses_so_far), machines[i] - target_dresses)
            # O valor máximo de abs(dresses_so_far) indica o número máximo de roupas que precisam ser movido em um único movimento
        
        return min_moves

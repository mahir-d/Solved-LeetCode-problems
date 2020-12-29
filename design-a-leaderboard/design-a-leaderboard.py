class Leaderboard:
​
    def __init__(self):
        self.leader_board = [0] * 10000
​
    def addScore(self, playerId: int, score: int) -> None:
         self.leader_board[playerId] += score
​
    def top(self, K: int) -> int:
        sorted_arr =  sorted(self.leader_board, reverse=True)
        return sum(sorted_arr[0:K])
​
    def reset(self, playerId: int) -> None:
        self.leader_board[playerId] = 0
​
​
# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)

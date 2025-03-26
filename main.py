# Check if git works-Germans
def main():
  # insert changes here and in other functions
  ...

if __name__ == "__main__":
  main()

class Game:
    def __init__(self, number):
        self.now_number = number
        self.player_points = 0
        self.ai_points = 0

    def move(self, divisor, is_human):
        """Izpilda gājienu, dalot skaitli un piešķirot punktus"""
        if self.now_number % divisor == 0:
            new_number = self.now_number // divisor
            if new_number % 2 == 0:
                if is_human:
                    self.ai_points -= 1
                else:
                    self.player_points += 1
            else:
                if is_human:
                    self.player_points += 1
                else:
                    self.ai_points += 1
            self.now_number = new_number
            return True
        return False

    def heuristic(self):
        return self.player_points - self.ai_points

    def Minimax(self, depth, is_maximizing):
        """Minimax algoritms"""
        if self.now_number <= 10 or depth == 0:
            return self.heuristic()

        moving_variants = [2, 3, 4]
        best_value = float('-inf') if is_maximizing else float('inf')

        for move in moving_variants:
            if self.now_number % move == 0:
                new_state = Game(self.now_number)  # Izveidojam jaunu spēles stāvokli
                new_state.player_points = self.player_points
                new_state.ai_points = self.ai_points
                new_state.move(move, is_maximizing)

                eval = new_state.Minimax(depth - 1, not is_maximizing)
                best_value = max(best_value, eval) if is_maximizing else min(best_value, eval)

        return best_value

    def Alpha_Beta(self, depth, alpha, beta, is_maximizing):
        """Alpha-Beta algoritms"""
        if self.now_number <= 10 or depth == 0:
            return self.heuristic()

        moving_variants = [2, 3, 4]

        if is_maximizing:
            max_eval = float('-inf')
            for move in moving_variants:
                if self.now_number % move == 0:
                    new_state = Game(self.now_number)
                    new_state.player_points = self.player_points
                    new_state.ai_points = self.ai_points
                    new_state.move(move, True)

                    eval = new_state.Alpha_Beta(depth - 1, alpha, beta, False)
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
            return max_eval
        else:
            min_eval = float('inf')
            for move in moving_variants:
                if self.now_number % move == 0:
                    new_state = Game(self.now_number)
                    new_state.player_points = self.player_points
                    new_state.ai_points = self.ai_points
                    new_state.move(move, False)

                    eval = new_state.Alpha_Beta(depth - 1, alpha, beta, True)
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            return min_eval
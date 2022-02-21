class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        
        self.width = width
        self.height = height
        self.food, self.f_idx = food, 0
        self.movements = {'R': (0, 1), 'D': (1, 0), 'U': (-1, 0), 'L': (0, -1)}
        self.snake_parts = [(0, 0)]
        self.snake_dict = {(0, 0): 1}
        
    def move(self, direction: str) -> int:
        
        head = self.snake_parts[-1]
        rx, cx = self.movements[direction]
        r, c = head[0] + rx, head[1] + cx
        
        if r < 0 or r >= self.height or c < 0 or c >= self.width:
            return -1
        
        # Found food, add new head
        if self.f_idx < len(self.food) and self.food[self.f_idx][0] == r and self.food[self.f_idx][1] == c:
            self.snake_parts.append((r, c))
            self.f_idx += 1
        else:
            old = self.snake_parts[-1]
            self.snake_parts[-1] = (r, c)
            for i in range(len(self.snake_parts) - 2, -1, -1):
                curr = self.snake_parts[i]
                self.snake_parts[i] = old
                old = curr
            del self.snake_dict[old]
         
        if (r, c) in self.snake_dict:
            return -1
        
        self.snake_dict[(r, c)] = 1    
        
        return len(self.snake_parts) - 1


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)

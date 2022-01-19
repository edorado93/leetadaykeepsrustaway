class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        even_avail = 0
        odd_avail = 0
        for idx in range(len(flowerbed)):
            
            if flowerbed[idx]:
                continue
            
            is_left_flower = flowerbed[idx - 1] == 1 if idx > 0 else False
            is_right_flower = flowerbed[idx + 1] == 1 if idx < (len(flowerbed) - 1) else False
            
            if not is_left_flower and not is_right_flower:
                even_avail += (idx % 2 == 0)
                odd_avail += (idx % 2 != 0)
        
        return even_avail >= n or odd_avail >= n

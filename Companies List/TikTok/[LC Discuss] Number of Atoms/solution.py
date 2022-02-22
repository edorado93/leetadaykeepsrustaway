class Solution:
    def countOfAtoms(self, formula: str) -> str:
        
        def get_count(idx):
            val = 0
            while idx < len(formula) and formula[idx].isdigit():
                val = (val * 10) + int(formula[idx])
                idx += 1
            return val if val > 0 else 1, idx
        
        def pop_multiply_and_merge(stack, count):
            
            top = stack[-1]
            for key in top:
                top[key] *= count
                
            if len(stack) > 1:
                stack.pop()
            
            next_top = stack[-1]
            for key in top:
                next_top[key] = next_top.get(key, 0) + top[key]
                
        def get_formula_name(idx):
            start = idx
            idx += 1
            while idx < len(formula):
                if formula[idx].islower():
                    idx += 1
                else:
                    break
                    
            return formula[start:idx], idx
        
        idx = 0
        stack = [{}]
        while idx < len(formula):
            
            char = formula[idx]
            
            if char == '(':
                stack.append({})
                idx += 1
                
            elif char == ')':
                count, idx = get_count(idx + 1)
                pop_multiply_and_merge(stack, count)
                
            else:
                formula_name, idx = get_formula_name(idx)
                count, idx = get_count(idx)
                stack[-1][formula_name] = stack[-1].get(formula_name, 0) + count
                
        keys = list(stack[-1].keys())
        keys.sort()
        
        string = ""
        for k in keys:
            string += k
            if stack[-1][k] > 1:
                string += str(stack[-1][k])
        
        return string

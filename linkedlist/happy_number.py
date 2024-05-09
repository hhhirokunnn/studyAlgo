class Step1:
    def isHappy(self, n: int) -> bool:
        seen = set()
        target_num = n
        while 1:
            if target_num == 1:
                return True
            if target_num in seen:
                return False
            seen.add(target_num)

            digits = []
            tmp = target_num
            while tmp > 0:
                digits.append(tmp % 10)
                tmp = tmp // 10

            target_num = 0
            while len(digits) > 0:
                d = digits.pop()
                target_num += d * d
            
        raise Error("unexpected")
            
# 問題把握4min
# 1. setをつかって計算した数字を保持。
# 2. digit を だしてarrayで保持。
# 3. setに含まれ、1が含まれていなければfalse
# 4. 2で出した数列を2乗してloop. matchしたらtrue
# time: O(log n) space O(log n)
# 解答まとめた5min
# 解答書いた16min

# この問題でFloyds Cycle-Finding は思いつけなかった。

class Step1:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            total_sum = 0
            while number > 0:
                digit, number = (number%10, number//10)
                total_sum += digit ** 2
            return total_sum

        slow = n
        fast = get_next(n)
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        return fast == 1
    
# 問題を構造化して考えると、同じ処理が繰り返されるターゲットがいることを考えると、納得できた。

class Step2:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            sum_num = 0
            while num > 0:            
                digit, num = (num % 10, num // 10)
                sum_num += digit ** 2
            return sum_num
            
        num = n
        seen = set()
        while num != 1 and num not in seen:
            seen.add(num)
            num = get_next(num)
        return num == 1

class Step2:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            sum_num = 0
            while num > 0:
                digit, num = (num%10, num//10)
                sum_num += digit ** 2
            return sum_num
        
        slow = n
        fast = get_next(n)

        while fast != 1 and slow != fast:
            slow=get_next(slow)
            fast=get_next(get_next(fast))
            
        return fast == 1

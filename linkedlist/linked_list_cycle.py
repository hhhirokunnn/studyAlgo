# 直近やったことがあったので、覚えてしまっていた。
# うさぎとかめのやつだとおもった。
# 進行差でぐるぐる回せばぶつかる。
# 計算量はtime: O(N)
# レスポンスはCycleの存在の有無だけで良いのでspace: O(1)

# Set使って実装してみる
# space O(N) time O(N)

class Step1:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        current = head
        while current:
            if current in seen:
                return True
            seen.add(current)
            current = current.next
        return False

# 覚えてしまっていたので時間かかっていない。
# 上記の解答なら、このまま、Cycleが始まるポインタを返すこともできる。

# とりあえず、うさぎとかめのやつでも書いてみた。
class Step1:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        fast = head
        slow = head
        
        while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
                if fast == slow:
                    return True
        return False

# この問題はStep２行かずに、同じ形式の問題解いてみる 

# 直近やったことがあったので、覚えてしまっていた。
# うさぎとかめのやつだとおもった。
# 時間差でぐるぐる回せばぶつかる。
# 計算量はtime: O(N)
# レスポンスはCycleの存在の有無だけで良いのでspace: O(1)

# Set使って実装してみる
# space O(N) time O(N)

class Solution:
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
# 上記の回答なら、setに入っているものがCycleが始まるポインタを返すこともできる。

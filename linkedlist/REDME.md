LinkedListはメモリ確保が動的に行われる
配列だと宣言時に要素を決定する必要があるため、それを超えるとスタックオーバーフローが発生する。
メモリを動的に確保した場合は明示的にメモリを開放しないとメモリリークする

https://www.geeksforgeeks.org/python-linked-list/

Vectorは初期化時に連続したメモリを確保する。

Vectorは各要素に対してランダムにアクセスすることが可能なので、要素の範囲に対して何かしらの処理をしたい場合に扱いやすい
LinkedListは前方から追っていくことになるのが厄介。


```python
class Node:
	def __init__(self, data):
		self.data=data
		sefl.next=None
class LinkedList:
	def __init__(self):
		self.head = None

	def reverse(self):
		prev = None
		curr = self.head
		while(curr):
			next = curr.next
			curr.next = prev
			curr = next
		self.head = prev			
```

あとでしらべる

trie
https://qiita.com/minaminao/items/caf6d8147c7e70b6ae63

bitmapped vector trie
https://qiita.com/b1ueskydragon/items/4a25b031ccb94b588bae#vector-trie


class Binary_Node:
	def __init__(self, x): # O(1)
		self.item = x
		self.left = None
		self.right = None
		self.parent = None
		# self.subtree_update() # wait for R07!

	def subtree_iter(self): # O(n)
		if self.left:
			yield from self.left.subtree_iter()
		yield self
		if self.right:
			yield from self.right.subtree_iter()

	def subtree_first(self): # O(h)
		if self.left:
			return self.left.subtree_first()
		else:
			return self

	def subtree_last(self): # O(h)
		if self.right:
			return self.right.subtree_last()
		else:
			return self

	def successor(self): # O(h)
		if self.right:
			return self.right.subtree_first()
		while self.parent and (self is self.parent.right):
			self = self.parent
		# this time, self.parent is None(if the first input self is the rightest node in the tree) or self is self.parent.left
		return self.parent

	def predecessor(self): # O(h)
		if self.left:
			return self.left.subtree_last()
		while self.parent and (self is self.parent.left):
			self = self.parent
		return self.parent
	
	def subtree_insert_before(A, B): # O(h)
		if A.left:
			A = A.left.subtree_last()
			A.right, B.parent = B, A
		else:
			A.left, B.parent = B, A
		# A.maintain() # wait for R07!
	
	def subtree_insert_after(A, B): # O(h)
		if A.right:
			A = A.right.subtree_first()
			A.left, B.parent = B, A
		else:
			A.right, B.parent = B, A
		# A.maintain() # wait for R07!
	
	def subtree_delete(A): # O(h)
		if A.left or A.right:
			if A.left:
				B = A.predecessor()
			else:
				B = A.successor()
			A.item, B.item = B.item, A.item
			return B.subtree_delete()
		if A.parent:# leaf node
			if A.parent.left is A:
				A.parent.left = None
			else:
				A.parent.right = None
		# A.parent.maintain() # wait for R07!
		return A
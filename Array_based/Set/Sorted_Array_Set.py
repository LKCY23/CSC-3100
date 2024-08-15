from Array_Seq import Array_Seq


class Sorted_Array_Set:
	def __init__(self):
		self.A = Array_Seq()  # O(1)

	def __len__(self):
		return len(self.A)  # O(1)

	def __iter__(self):
		yield from self.A  # O(n)

	def iter_order(self):
		# accually calling the __iter__ method
		yield from self  # O(n)

	def build(self, X):  # O(?)
		self.A.build(X)
		self._sort()

	def _sort(self):  # O(?)
		# Add sorting logic here
		pass

	def _binary_search(self, k, i, j):  # O(log n)
		# return the insert location
		if i >= j:
			return i
		m = (i + j) // 2
		x = self.A.get_at(m)
		if x.key > k:
			return self._binary_search(k, i, m - 1)
		if x.key < k:
			return self._binary_search(k, m + 1, j)
		return m

	# Rest of the code remains the same

	def find_min(self):  # O(1)
		if len(self) > 0:
			return self.A.get_at(0)
		else:
			return None

	def find_max(self):  # O(1)
		if len(self) > 0:
			return self.A.get_at(len(self) - 1)
		else:
			return None

	def find(self, k):  # O(log n)
		if len(self) == 0:
			return None
		i = self._binary_search(k, 0, len(self) - 1)
		x = self.A.get_at(i)
		if x.key == k:
			return x
		else:
			return None

	def find_next(self, k):  # O(log n)
		if len(self) == 0:
			return None
		i = self._binary_search(k, 0, len(self) - 1)
		x = self.A.get_at(i)
		if x.key > k:
			return x
		# no matter whether k is existed or not, i+1 is the next
		if i + 1 < len(self):
			return self.A.get_at(i + 1)
		else:
			return None

	def find_prev(self, k):  # O(log n)
		if len(self) == 0:
			return None
		i = self._binary_search(k, 0, len(self) - 1)
		x = self.A.get_at(i)
		if x.key < k:
			return x
		if i > 0:
			return self.A.get_at(i - 1)
		else:
			return None

	def insert(self, x):  # O(n)
		if len(self.A) == 0:
			self.A.insert_first(x)
		else:
			i = self._binary_search(x.key, 0, len(self.A) - 1)
			k = self.A.get_at(i).key
			if k == x.key:
				self.A.set_at(i, x)
				return False
			if k > x.key:
				self.A.insert_at(i, x)
			else:
				self.A.insert_at(i + 1, x)
			return True

	def delete(self, k):  # O(n)
		i = self._binary_search(k, 0, len(self.A) - 1)
		assert self.A.get_at(i).key == k
		return self.A.delete_at(i)

    #
	# different sorting logic
    #
	def selection_sort(A):  # Selection sort array A
		for i in range(len(A) - 1, 0, -1):  # O(n) loop over array
			m = i  # O(1) initial index of max
			for j in range(i):  # O(i) search for max in A[:i]
				if A[m] < A[j]:  # O(1) check for larger value
					m = j  # O(1) new max found
			A[m], A[i] = A[i], A[m]  # O(1) swap
	# for each i, the former part is sorted, the max element in the latter part is found and exchanged with the last element of the former part
	# O(n^2) time complexity
	# swaps O(n) times
	# unstable, because the order of equal elements is not preserved

	def insertion_sort(A):  # Insertion sort array A
		for i in range(1, len(A)):  # O(n) loop over array
			j = i  # O(1) initialize pointer
			while j > 0 and A[j] < A[j - 1]:  # O(i) loop over prefix
				A[j - 1], A[j] = A[j], A[j - 1]  # O(1) swap
				j = j - 1  # O(1) decrement j
    # for each i, the former part is sorted, the element pointed is  exchanged with the former element until the former element is smaller than the pointed element
	# O(n^2) time complexity
	# O(1) space complexity
	# O(n) stable
	# O(1) adaptive
	# O(n) comparisons
	# O(n^2) swaps
	# O(n) extra space


	def merge_sort(self, a=0, b=None):  # Sort sub-array A[a:b]
		A = self.A  # O(1) get array
		if b is None:  # O(1) initialize
			b = len(A)  # O(1)
		if 1 < b - a:  # O(1) size k = b - a
			c = (a + b + 1) // 2  # O(1) compute center
			self.merge_sort(A, a, c)  # T(k/2) recursively sort left
			self.merge_sort(A, c, b)  # T(k/2) recursively sort right
			L, R = A[a:c], A[c:b]  # O(k) copy
			i, j = 0, 0  # O(1) initialize pointers
			while a < b:  # O(n)
				if (j >= len(R)) or (i < len(L) and L[i] < R[j]):  # O(1) check side
					A[a] = L[i]  # O(1) merge from left
					i = i + 1  # O(1) increment left pointer
				else:
					A[a] = R[j]  # O(1) merge from right
					j = j + 1  # O(1) increment right pointer
				a = a + 1  # O(1) increment merge pointer
	# for each k, the array is divided into two parts, and then merged into a sorted array
	# O(n log n) time complexity
	# O(n) space complexity
	# for stability:
	# 	if (j >= len(R)) or (i < len(L) and L[i] <= R[j]): # 将 < 改为 <=
	#     A[a] = L[i]
	#     i = i + 1
	# 	else:
	#     A[a] = R[j]
	#     j = j + 1
	# preprocessing O(n) time complexity
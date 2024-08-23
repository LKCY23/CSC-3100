class DirectAccessArray:
		def __init__(self, u):
			self.A = [None] * u  # O(u)

		def find(self, k):
			return self.A[k]  # O(1)

		def insert(self, x):
			self.A[x.key] = x  # O(1)

		def delete(self, k):
			self.A[k] = None  # O(1)

		def find_next(self, k):
			for i in range(k, len(self.A)):  # O(u)
				if self.A[i] is not None:
					return self.A[i]

		def find_max(self):
			for i in range(len(self.A) - 1, -1, -1):  # O(u)
				if self.A[i] is not None:
					return self.A[i]

		def delete_max(self):
			for i in range(len(self.A) - 1, -1, -1):  # O(u)
				x = self.A[i]
				if x is not None:
					self.A[i] = None
					return x


class Object:
	def __init__(self, key):
		self.key = key

			
if __name__ == "__main__":
	da_array = DirectAccessArray(10)

	# Test the insert function
	da_array.insert(Object(5))
	da_array.insert(Object(2))
	da_array.insert(Object(8))

	# Test the find function
	print(da_array.find(5).key)  # Output: 5
	print(da_array.find(2).key)  # Output: 2
	print(da_array.find(8).key)  # Output: 8

	# Test the delete function
	da_array.delete(2)
	print(da_array.find(2))  # Output: None

	# Test the find_next function
	print(da_array.find_next(5).key)  # Output: 8

	# Test the find_max function
	print(da_array.find_max().key)  # Output: 8

	# Test the delete_max function
	da_array.delete_max()
	print(da_array.find_max())  # Output: None
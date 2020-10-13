class Node(object):
	def __init__(self, data):
		self.data = data
		self.left = self.right = None

class BinarySearchTree(object):
	def __init__(self):
		self.root = None
	def insert(self, data):
		self.root = self.__insert__value(self.root, data)
		return self.root is not None
	def __insert__value(self, node, data):
		if node is None:
			node = Node(data)
		else:
			if data <= node.data:
				node.left = self.__insert__value(node.left, data)
			else:
				node.right = self.__insert__value(node.right, data)
		return node
	def find(self, key):
		return self._find_value(self.root, key)
	def __find__value(self, root, key):
		if root is None or root.data == key:
			return root is not None
		elif key < root.data:
			return self.__find__value(root.left, key)
		else:
			return self.__find__value(root.right, key)
	def delete(self, key):
		self.root, deleted = self.__delete__value(self.root, key)
		return deleted
	def __delete__value(self, node, key):
		if node is None:
			return node, False
		deleted = False
		if key == node.data:
			deleted = True
			if node.left and node.right:
				parent, child = node, node.right
				while child.left is not None:
					parent, child = child, child.left
				child.left = node.left
				if parent != node:
					parent.left = child.right
					child.right = node.right
				node = child
			elif node.left or node.right:
				node = node.left or node.right
			else:
				node = None
		elif key < node.data:
			node.left, deleted = self.__delete__value(node.left, key)
		else:
			node.right, deleted = self.__delete__value(node.right, key)
		return node, deleted


	def preorder(self):
		def _pre_order(root):
			if root is None:
				pass
			else:
				print(root.data)
				_pre_order(root.left)
				_pre_order(root.right)
		_pre_order(self.root)

	def inorder(self):
		def _in_order(root):
			if root is None:
				pass
			else:
				_in_order(root.left)
				print(root.data)
				_in_order(root.right)
		_in_order(self.root)

	def postorder(self):
		def _post_order(root):
			if root is None:
				pass
			else:
				_post_order(root.left)
				_post_order(root.right)
				print(root.data)
		_post_order(self.root)
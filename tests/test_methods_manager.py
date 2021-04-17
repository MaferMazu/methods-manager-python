import unittest
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from methods_manager import *

class TestMethodsManager(unittest.TestCase):
    def test_creation(self):
        methods_manager = MethodsManager()
        self.assertEqual(methods_manager.heap,{})

    def test_insert(self):
        manager = MethodsManager()
        manager.insert(["CLASS","A",1,2,3,4,5,6,7])
        self.assertEqual(manager.heap,{"A":{"super":None, "methods":[1,2,3,4,5,6,7]}})

    def test_insert_with_super(self):
        manager=MethodsManager()
        manager.insert(["CLASS","A",1,2,3,4,5,6,7])
        manager.insert(["CLASS","B",":","A",3,7])
        self.assertEqual(manager.heap,{"A":{"super":None, "methods":[1,2,3,4,5,6,7]}, "B":{"super":"A", "methods":[3,7]}})

    def test_invalid_super(self):
        manager = MethodsManager()
        manager.insert(["CLASS","A",1,2,3,4,5,6,7])
        manager.insert(["CLASS","B",":","T",3,7])
        self.assertEqual(manager.heap,{"A":{"super":None, "methods":[1,2,3,4,5,6,7]}})

    def test_invalid_name(self):
        manager = MethodsManager()
        manager.insert(["CLASS","h",3,7])

    def test_have(self):
        manager=MethodsManager()
        manager.insert(["CLASS","A",1,2,3,4,5,6,7])
        response=manager.have("A")
        self.assertEqual(response,True)

    def test_have_2(self):
        manager=MethodsManager()
        manager.insert(["CLASS","A",1,2,3,4,5,6,7])
        response=manager.have("B")
        self.assertEqual(response,False)

    def test_insert_simple(self):
        manager=MethodsManager()
        manager.insert_simple("A",None,1,2,3,4,5,6,7)
        self.assertEqual(manager.heap,{"A":{"super":None, "methods":[1,2,3,4,5,6,7]}})

    def test_search_method_base(self):
        manager=MethodsManager()
        manager.insert(["CLASS","A",1,2])
        response=manager.search_methods("A")
        self.assertEqual(
            response,
            "1 -> A :: 1\n2 -> A :: 2\n")

    def test_search_method_fail(self):
        manager=MethodsManager()
        manager.insert(["CLASS","A",1,2])
        response=manager.search_methods("B")
        self.assertEqual(response, None)

    def test_search_method(self):
        manager=MethodsManager()
        manager.insert(["CLASS","A",1,2,3,4,5])
        manager.insert(["CLASS","B",":","A",3,7])
        response=manager.search_methods("B")
        self.assertEqual(
            response,
            "1 -> A :: 1\n2 -> A :: 2\n3 -> B :: 3\n4 -> A :: 4\n5 -> A :: 5\n7 -> B :: 7\n")


if __name__ == "__main__":
    unittest.main()
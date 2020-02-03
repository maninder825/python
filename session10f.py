"""

Types of Recursion
1. direct recursion
2. Indirect recursion
3. Tail recursion

"""

def fun():

    fun()  #Direct Recursion


def fun1():

    fun2(); # Indirect Recursion

def fun2()

    fun1()


def tailRec():
    #...
    #...

    tailRec()  # last statement is execution of function


# HW : Implement Insertion sort with Recursion.


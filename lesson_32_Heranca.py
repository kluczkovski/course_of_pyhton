class A():

    def __init__(self):
        print("init A")
        super().__init__()

class B():
    def __init__(self):
        print("init B")
        super().__init__()

class C(A,B):
    def __init__(self):
        print("init C")
        super().__init__()


C()

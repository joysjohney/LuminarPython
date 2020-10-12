class Parent:
    def m1(self):
        print("inside parent1")

class Child:
    def m2(self):
        print("inside child")

class SubChild(Child,Parent):
    def m3(self):
        print("inside subchild")

#parent
p=Parent()
p.m1()

#child
c=Child()
c.m2()
c.m1()

#subchild
s=SubChild()
s.m1()
s.m2()
s.m3()
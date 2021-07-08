
class Calc():
      def __init__(self):
          self.total = 0
          self.add_numbers = False
      
      def one(self): 
        if self.add_numbers:
           self.total += 1
           self.add_numbers = False
        else:
          self.total = 1
        return self

      def two(self): 
        if self.add_numbers:
           self.total += 2
           self.add_numbers = False
        else:
          self.total = 2
        return self

      def three(self): 
        if self.add_numbers:
           self.total += 3
           self.add_numbers = False
        else:
          self.total = 3
        return self

      def plus(self): 
        self.add_numbers = True
        return self

      def equals(self):
          return self.total

assert Calc().one().equals() == 1
assert Calc().three().plus().one().equals()  == 4
assert Calc().two().plus().three().plus().one().plus().one().plus().three().equals() == 10
assert Calc().one().plus().two().equals() == 3
assert Calc().two().plus().three().plus().one().plus().one().equals() == 7
assert Calc().one().plus().three().plus().two().plus().one().plus().three().equals() == 10
    

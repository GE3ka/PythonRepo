class MathDojo:

    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        # your code here
        self.result+=num
        for i in range (len(nums)):
            self.result += nums[i]
        
        return self
    def subtract(self, num, *nums):
        # your code here
        self.result-=num
        for i in range (len(nums)):
            self.result -= nums[i]
        return self
# create an instance:
md = MathDojo()
md2=MathDojo()
md3=MathDojo()
# to test:
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5
# run each of the methods a few more times and check the result!
y=md2.add(5,2,8,9).subtract(3,8,9).add(5,1).result #10
print(y)
z=md3.add(4,2).add(3).subtract(1).result #8
print(z)
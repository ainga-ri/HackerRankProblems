class Difference:
    def __init__(self, a):
        self.__elements = a
	# Add your code here
    maximumDifference = 0
    def computeDifference(self):
        for i in range(len(a)):
            for j in range(i, len(a)):
                value = abs(a[i] - a[j])
                if(a[i] != a[j] and value > self.maximumDifference):
                    self.maximumDifference= value
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
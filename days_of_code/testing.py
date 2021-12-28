def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx

'''
# I thought i needed to create a class in order to get an input, but testing is about
# I give the input and test the functions

class TestDataEmptyArray():
    def get_array(self):
        return list()

class TestDataUniqueValues():
    def get_array(self):
        self.array = list(map(int, input().rstrip().split()))
        if (len(self.array) >= 2):
            for i in range(1,len(self.array)):
                if (self.array[i-1] == self.array[i]):
                    self.array.pop(i)
            return self.array

    def get_expected_result(self):
        self.array = list(map(int, input().rstrip().split()))
        seq = self.array
        if len(seq) == 0:
            raise ValueError("Cannot get the minimum value index from an empty sequence")
        min_idx = 0
        for i in range(1, len(seq)):
            if seq[i] < seq[min_idx]:
                min_idx = i
        return min_idx

class TestDataExactlyTwoDifferentMinimums(TestDataUniqueValues):
    def get_array(self):
        super().get_array()
    def get_expected_result(self):
        super().get_expected_result()
'''

#This is the testing

class TestDataEmptyArray(object):
    @staticmethod
    def get_array():
        return list()

class TestDataUniqueValues(object):
    @staticmethod
    def get_array():
        return [2,4,7]
    @staticmethod
    def get_expected_result():
        return 0

class TestDataExactlyTwoDifferentMinimums(object):
    @staticmethod
    def get_array():
        return [2,4,2]
    @staticmethod
    def get_expected_result():
        return 0  

def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")


class Test(object):
    @staticmethod
    def assert_equals(a, b):
        if len(a) != len(b):
            return 0
        for i, _ in enumerate(a):
            if a[i] != b[i]:
                return 0
        return 1

    @staticmethod
    def assert_equal(a, b):
        if a != b:
            print("fail", a, b)
        else:
            print("success", a, b)


if __name__ == "__main__":
    print(Test.assert_equals([1, 2, 3], [1, 2, 3]))
    print(Test.assert_equals([2, 2, 3], [1, 2, 3]))
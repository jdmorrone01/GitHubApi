import unittest

from gitdata import getGitRep

class TestGit(unittest.TestCase):
    def testRich(self):
        self.assertEquals(getGitRep('richkempinski'),True)


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()


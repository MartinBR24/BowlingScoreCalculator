import unittest
import os
import sys
# Add the directory containing your module to the Python path (wants absolute paths)
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/BowlingScoreCalculator.py");
# Do the import
import BowlingScoreCalculator

class BowlingScoreCalculatorTests(unittest.TestCase):
    def testAssignmentExample(self):
        exampleScores = [[3,7],[10,0],[8,2],[8,1],[10,0],[3,4],[7,0],[5,5],[3,2],[2,5]];
        exampleSums = [20,40,58,67,84,91,98,111,116,123];
        
        calc = BowlingScoreCalculator.BowlingScoreCalculator();
        actualSums = calc.CalculateFrameSums(exampleScores);
        self.assertEqual(actualSums,exampleSums);

def main():
    unittest.main();

if __name__ == '__main__':
    main();

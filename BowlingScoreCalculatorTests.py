import unittest
import os
import sys
# Add the directory to script under test to the Python path (wants absolute paths)
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + "/BowlingScoreCalculator.py");
# Do the import
import BowlingScoreCalculator

class BowlingScoreCalculatorTests(unittest.TestCase):

    def testAssignmentExample(self):
        # Test that calculator gets correct result for the example set given in the assigmenmt
        exampleScores = [[3,7],[10,0],[8,2],[8,1],[10,0],[3,4],[7,0],[5,5],[3,2],[2,5]];
        exampleSums = [20,40,58,67,84,91,98,111,116,123];

        calc = BowlingScoreCalculator.BowlingScoreCalculator();
        actualSums = calc.CalculateFrameSums(exampleScores);
        self.assertEqual(actualSums,exampleSums);

    def testIntegration_CorrectTokenStatus(self):
        # Test that API Integration gets correct and functioning token status. (success code 200)
        calc = BowlingScoreCalculator.BowlingScoreCalculator();
        response = calc.GetPointsFromAPI();
        result = calc.PostSumsToAPI([0,0],response.json()["token"]).status_code;
        self.assertTrue(result==200);

    def testIntegration_IncorrectTokenStatus(self):
        # Test that API Integration responds as expected when given incorrect token (Not success code 200)
        calc = BowlingScoreCalculator.BowlingScoreCalculator();
        result = calc.PostSumsToAPI([0,0],"IncorrectToken123").status_code;
        self.assertFalse(result==200);

def main():
    unittest.main();

if __name__ == '__main__':
    main();

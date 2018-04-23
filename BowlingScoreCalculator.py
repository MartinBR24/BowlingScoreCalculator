import requests
import json

class BowlingScoreCalculator():

    APIUrl = "http://13.74.31.101/api/points";
    points = {};
    token = "";
    sums = [];

    def CalculateFrameSums(self, pointsArray=[]):
        returnArray = [];
        return "Unimplemented"

    def GetPointsFromAPI(self):
        #Get bowling point frames and API POST Token
        response = requests.get(self.APIUrl);
        JSON = response.json();
        #Save to variables

        self.points = JSON['points'];
        self.token = JSON["token"];

    def PostSumsToAPI(self):
        sums = self.CalculateFrameSums();

        postmsg = {"points":sums};
        response = requests.post(self.APIUrl,json=postmsg,params={"token":self.token});
        print "Token status code: " + str(response.status_code);
        #Class end


#If script is run directly, as opposed to imported.
if __name__ == "__main__":

    calc = BowlingScoreCalculator();
    calc.GetPointsFromAPI();
    calc.PostSumsToAPI();

import requests
import json

class BowlingScoreCalculator():
    APIUrl = "";

    def __init__(self, APIUrl = "http://13.74.31.101/api/points"):
        self.APIUrl = APIUrl;

    def CalculateFrameSums(self, pointsArray):
        returnArray = [];
        return "Unimplemented"

    def GetPointsFromAPI(self):
        #Get bowling point frames and API POST Token
        response = requests.get(self.APIUrl);

        return response;

    def PostSumsToAPI(self,sums,token):
        postmsg = {"points":sums};
        response = requests.post(self.APIUrl,json=postmsg,params={"token":token});
        return response;

#Class end


#If script is run directly, as opposed to imported.
if __name__ == "__main__":

    calc = BowlingScoreCalculator();
    JSON = calc.GetPointsFromAPI().json();
    response = calc.PostSumsToAPI(JSON["points"],JSON["token"]);
    print "Token status code: " + str(response.status_code);
    print "Calculation success: " + str(response.json()["success"]);

import requests
import json
import time

class BowlingScoreCalculator():
    APIUrl = "";

    def __init__(self, APIUrl = "http://13.74.31.101/api/points"):
        self.APIUrl = APIUrl;

    def CalculateFrameSums(self, pointsArray):
        returnList = [];
        currentSum = 0;
        for i,frame in enumerate(pointsArray):
            if i <= 9:
                if frame[0]==10 and frame[1]==0:
                    # print "Strike";
                    currentSum += (10);
                    if len(pointsArray)-1 > i:
                        currentSum += pointsArray[i+1][0]+pointsArray[i+1][1]
                        if pointsArray[i+1][0]==10 and len(pointsArray)-1 > i+1:
                            # Two strikes in a row
                            currentSum += pointsArray[i+2][0];

                elif frame[0]+frame[1]==10:
                    # print "Spare";
                    currentSum += 10;
                    if len(pointsArray)-1 > i:
                        currentSum += pointsArray[i+1][0];

                else:
                    # print "Open Frame";
                    currentSum += (frame[0]+frame[1]);

                returnList.append(currentSum);

        return returnList;

    def GetPointsFromAPI(self):
        #Get bowling point frames and API POST Token
        response = requests.get(self.APIUrl);
        if response.status_code == 429:
            # Too many attempts. Wait a little
            time.sleep(10);
            return self.GetPointsFromAPI();
        return response;

    def PostSumsToAPI(self,sums,token):
        postmsg = {"points":sums};
        response = requests.post(self.APIUrl,json=postmsg,params={"token":token});
        if response.status_code == 429:
            # Too many attempts. Wait a little
            time.sleep(10);
            return self.PostSumsToAPI(sums,token);
        return response;

#Class end


#If script is run directly, as opposed to imported.
if __name__ == "__main__":

    calc = BowlingScoreCalculator();
    JSON = calc.GetPointsFromAPI().json();
    print "Scores gotten from API: ";
    print JSON["points"];
    print "";
    sums = calc.CalculateFrameSums(JSON["points"]);
    print "Calculated sums: "
    print sums;
    print "";
    response = calc.PostSumsToAPI(sums,JSON["token"]);
    print "Token status code: " + str(response.status_code);
    print "Calculation success: " + str(response.json()["success"]);

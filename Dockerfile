#Set the base
FROM ubuntu
#Author
MAINTAINER martinbr24 <mbagge@outlook.com>

RUN apt-get update && apt-get install python-pip -y
RUN pip install requests
RUN mkdir /BowlingScoreCalculator
ADD Scripts /BowlingScoreCalculator/Scripts

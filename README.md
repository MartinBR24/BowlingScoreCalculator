# BowlingScoreCalculator
Besvarelsen er skrevet i python, fordi dette kræver minimalt framework og kører på alle platforme.
## Docker container
Et Image med scripts er sat op og klar til at køre under **martinbr24/bowlingimage**

Container kan startes og køre scripts direkte ved hjælp af følgende kommando:

>$`docker run martinbr24/bowlingimage /bin/bash -c "python /BowlingScoreCalculator/Scripts/BowlingScoreCalculatorTests.py && python /BowlingScoreCalculator/Scripts/BowlingScoreCalculator.py`

Ovenstående kører først alle tests, og hvis disse består køres scriptet, hvilket giver lidt flere prints

*OBS: kan godt være der skal "sudo" foran hvis det køres fra Linux*


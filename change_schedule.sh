#!/bin/bash

echo "do you want to change the start time? yes or no?"
read CHOICE1
if [ $CHOICE1 -eq "yes" ]
then
    echo "Please mention the start time hours (0-24)"
    read STARTTIMEHR
    echo "Please mention the minute at which the ec2 should start (0-60)"
    read STARTTIMEMIN
    aws events put-rule --name "sandeepEC2Start" --schedule-expression "cron($STARTTIMEMIN $STARTTIMEHR ? * * *)"
    echo "Start Time has been changed to $STARTTIMEHR : $STARTTIMEMIN"

    CHOICE2="NULL"
    echo "do you want to change the stop time? yes or no?"
    read CHOICE2
    if [ $CHOICE2 -eq "yes" ]
    then
        echo "Please mention the stop time hours (0-24)"
        read STOPTIMEHR
        echo "Please mention the minute at which the ec2 should stop (0-60)"
        read STOPTIMEMIN
        aws events put-rule --name "sandeepEC2Stop" --schedule-expression "cron($STOPTIMEMIN $STOPTIMEHR ? * * *)"
        echo "Stop Time has been changed to $STOPTIMEHR : $STOPTIMEMIN"
    elif [[ $CHOICE2 -eq "no" ]]
    then
        echo "Stop Time has not been chaged"
    else
        echo "Invalid Input..exitting"
    fi


elif [ $CHOICE1 -eq "no" && $CHOICE2 -eq "NULL" ]
then
    echo "do you want to change the stop time? yes or no?"
    read CHOICE3
    if [ $CHOICE3 -eq "yes" ]
    then
        echo "Please mention the stop time hours (0-24)"
        read STOPTIMEHR1
        echo "Please mention the minute at which the ec2 should stop (0-60)"
        read STOPTIMEMIN1
        aws events put-rule --name "sandeepEC2Stop" --schedule-expression "cron($STOPTIMEMIN1 $STOPTIMEHR1 ? * * *)"
        echo "Stop Time has been changed to $STOPTIMEHR1 : $STOPTIMEMIN1"
    elif [ $CHOICE3 -eq "no" ]
    then
        echo "Nothing has been changed"
    else
        echo "Invalid Input..exitting"
        exit
    fi
else
    echo "Invalid Input...exitting"
fi


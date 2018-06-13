#!/bin/bash

aws events put-rule --name "sandeepEC2Start" --schedule-expression "cron(0 9 * * ? *)"
aws events put-rule --name "sandeepEC2Stop" --schedule-expression "cron(0 21 * * ? *)"



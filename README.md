# monti-time-logger
Explore time use by logging activities at random moments throughout the day. 

## Description

Sends texts via email with a link to a google form for logging what activity you are currently doing. These tasks are sent 
at random times throughout the day using a crontab and a bash script. The emails are sent using a gmail account.

## Installing

- Clone repository
- Create `gmailInfo.yml` and `userInfo.yml` config files based on the templates.  
- Create link to repository in the home directory
- Copy the template [google form](https://docs.google.com/forms/d/1c6tDGrUaMSmeOvNbTceTQ-8YrgeXgqcx2PyFyX2eo3k/edit?usp=sharing) to your google drive and edit as you see fit.
- Start a cron job to run the randomRunner.sh script at midnight every night. In Ubuntu this editing the crontab, ` $ crontab -e`, and adding the following lines 
```
SHELL=/bin/bash
0 0 * * * .monti-time-logger/randomRunner.sh > cronlogs/activityLogger.log
```

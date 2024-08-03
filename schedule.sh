#!/bin/bash
# every 4 hours if on wifi and charging, run backup
termux-job-scheduler -s "dotenvx run -- python backup.py" --period-ms 14400000 --network unmetered --charging true

pathToScript=$'.monti-time-logger/sendFormRequest.py'
formsPerDay=1
maxdelay=$((60*24))  # 24 hours converted to minutes
for ((i=1; i<=$formsPerDay; i++)); do
    delay=$(($RANDOM%maxdelay)) # pick an independent random delay for each of the 20 runs
    (sleep $((delay*60)); /usr/bin/python ~/$pathToScript) & # background a subshell to wait, then run the php script
done

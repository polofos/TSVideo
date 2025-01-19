#! /bin/bash
while read line; do
    wget $line
done < TS_URLS.txt

for f in *.ts ; do
   echo file \'$f\' >> list.txt;
done

ffmpeg -f concat -safe 0 -i list.txt -c copy Temp.ts

ffmpeg -i Temp.ts -map 0 -c copy $1

if [ $? -ne 0 ]; then  
    echo "Something went wrong :("  
    exit 1
else
    rm *.ts list.txt TS_URLS.txt
fi
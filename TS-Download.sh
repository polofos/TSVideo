#! /bin/bash
#while read line; do
#wget $line
#done < TS_URLS.txt
for f in *.ts ; do
echo file \'$f\' >> list.txt;
done
ffmpeg -f concat -safe 0 -i list.txt -c copy Sonic2.ts
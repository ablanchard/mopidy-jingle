#! /bin/bash
# Requires espeak and sox

mkdir -p /home/jingles
export counter=0
cat /jingles-en.txt | while read line 
do
   espeak -s 120 "$line" -w /tmp/tmp.wav && sox /tmp/tmp.wav -r 96000 /home/jingles/$counter.wav
   counter=$((counter+1))
done

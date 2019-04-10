#!/bin/bash
##Path to pcap files.
FILEPATH0=/root/Desktop/uav-classifier/packets/cap/**/*.cap
FILEPATH1=/root/Desktop/uav-classifier/packets/pcap/**/*.pcap
FILEPATH2=/root/Desktop/uav-classifier/packets/pcap/**/*.pcapng
##gets all files that are in the Folder

shopt -s globstar
for file in $FILEPATH0; do
	echo $(basename $file)
	outfile=$(echo $file | rev | cut -c 4- | rev | echo "$(cat -)pcap")
	editcap -F pcap -r $file > $outfile &
	echo "Created: $outfile"
	
	for outfile in $FILEPATH0; do
		echo $(basename $outfile)
		chmod 755 $outfile
		jsonoutfile=$(echo $file | rev | cut -c 4- | rev | echo "$(cat -)json")
		tshark -T json -r $outfile > $jsonoutfile &
		echo "Created: $jsonoutfile"
	done
done
for file in $FILEPATH1; do
        echo $(basename $file)
  ##Takes the old file name and removes the last 4 chars.
  ##Then adds "json" to the end of the string.
        chmod 755 $file
        outfile=$(echo $file | rev | cut -c 5- | rev | echo "$(cat -)json")
  ##Converts a pcap file to a json file and outputs the json file
  ##where the pcap file is.
        #tshark -r $file -T json > $file.json &
        tshark -T json -r $file > $outfile &
        echo "Created: $outfile"
done
for file in $FILEPATH2; do
        echo $(basename $file)
        chmod 755 $file
        outfile=$(echo $file | rev | cut -c 7- | rev | echo "$(cat -)json")
        tshark -T json -r $file > $outfile &
        echo "Created: $outfile"
done


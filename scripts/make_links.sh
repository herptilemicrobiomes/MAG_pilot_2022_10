#!/usr/bin/bash -l
IFS=,
SAMPLES=samples.csv
SOURCE=/bigdata/stajichlab/shared/projects/SeqData/UCR_seq/UCB_20221213_JStajich
TARGET=input
mkdir -p $TARGET  # make dir if doesn't exist

cat $SAMPLES | while read PREFIX NAME
do	
	for DIRECTION in 1 2
	do
		ln -s $SOURCE/${PREFIX}_*_R${DIRECTION}_001.fastq.gz $TARGET/${NAME}_${DIRECTION}.fastq.gz
	done
done

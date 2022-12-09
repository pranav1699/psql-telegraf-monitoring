#!/bin/sh
set -m
echo $INPUT_DATABASE
echo $OUTPUT_DATABASE
python3 --version
streamlit --version
./telegraf version
if [ "$INPUT_DATABASE" != "" ]
then
        ./telegraf --config telegraf_postgres.conf &
        streamlit run ./app.py
else
      echo $INPUT_DATABASE
fi
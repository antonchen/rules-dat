#!/bin/bash
# Author: Anton Chen <contact@antonchen.com>
# Create Date: 2024-01-06 20:47:56
# Last Modified: 2024-01-06 20:47:57
# Description: 
DB_FILE="$GITHUB_WORKSPACE/geosite-lite.db"
SING_SRS="$GITHUB_WORKSPACE/sing"

cd $GITHUB_WORKSPACE

if [ ! -f "$DB_FILE" ]; then
    echo "File $DB_FILE not found!"
    exit 1
fi

if [ ! -d "$SING_SRS" ]; then
    mkdir -p "$SING_SRS"
fi

wget -q -c https://github.com/SagerNet/sing-box/releases/download/v1.8.0/sing-box-1.8.0-linux-amd64.tar.gz -O sing-box.tar.gz
tar -xzf sing-box.tar.gz
mv sing-box-1.8.0-linux-amd64/sing-box sing-box
rm -rf sing-box-1.8.0-linux-amd64 sing-box.tar.gz

GOE_LIST=($($GITHUB_WORKSPACE/sing-box geosite list -f $DB_FILE | sed 's/ (.*)$//g'))
for ((i = 0; i < ${#GOE_LIST[@]}; i++)); do
    $GITHUB_WORKSPACE/sing-box geosite export ${GOE_LIST[i]} -o $SING_SRS/${GOE_LIST[i]}.json -f $DB_FILE
    $GITHUB_WORKSPACE/sing-box rule-set compile $SING_SRS/${GOE_LIST[i]}.json -o $SING_SRS/${GOE_LIST[i]}.srs
done
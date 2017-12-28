#!/bin/bash

set -ex
cd `dirname $0`

DATE=$(date +%\Y%\m%\d)

mkdir ${DATE}

sed "s/\${DATE}/${DATE}/g" create_table.sql > ./${DATE}/create_table_${DATE}.sql
sed "s/\${DATE}/${DATE}/g" main.py > ./${DATE}/main_${DATE}.py

cd ${DATE}

mysql -h178.62.122.173 -uzhouminping -pqazwsx house_info < create_table_${DATE}.sql
python main_${DATE}.py > out.log 2> error.log

echo ${DATE} success
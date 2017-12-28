#!/bin/bash

price_reduction_distribution=$(mysql -h178.62.122.173 -uzhouminping -pqazwsx house_info < price_reduction_distribution.sql)
echo "${price_reduction_distribution//$'\t'/,}" > price_reduction_distribution.csv


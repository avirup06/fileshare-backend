cd .\fileshare;
rm -rf .test.txt;
current_date_time=$(date);
echo $current_date_time >> .test.txt;
python3 -m pytest tests --cov=fileshare >> .test.txt
rm -rf tests\test_database.db
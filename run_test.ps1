Set-Location .\fileshare
Remove-Item .test.txt
Get-Date >> .test.txt
python -m pytest tests --cov=fileshare >> .test.txt
Remove-Item tests\test_database.db
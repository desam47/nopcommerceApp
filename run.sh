#!/bin/bash
#echo "Hello world"
/home/dips/pythonProject/nopcommerceApp/venv/bin/pytest -s -v -m "sanity" --html=Reports/report.html testCases/ --browser chrome
#/home/dips/pythonProject/nopcommerceApp/venv/bin/pytest -v -m "sanity or regression" --html=Reports/report.html testCases/ --browser chrome
#/home/dips/pythonProject/nopcommerceApp/venv/bin/pytest -v -m "sanity and regression" --html=Reports/report.html testCases/ --browser chrome
#/home/dips/pythonProject/nopcommerceApp/venv/bin/pytest -v -m "regression" --html=Reports/report.html testCases/ --browser chrome

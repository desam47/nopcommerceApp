#! /bin/sh

pytest -v -m "sanity" --html=Reports/report.html testCases/ --browser chrome

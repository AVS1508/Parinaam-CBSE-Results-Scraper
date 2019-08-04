# CBSE-Results-Scraper

## Purpose
<strong> CBSE-Results-Scraper </strong> is a command-line Python application that scrapes and downloads student reports of CBSE (Central Board of Secondary Education) Class XII Results 2019 from http://cbseresults.nic.in. 

## Disclaimer
This project is <em>solely intended for educational purposes</em>! Please do not use it for any other reason than to learn about web scraping. There might be <em>serious consequences</em> to using this script for breaching someone's privacy and/or publishing results that are not yours to share!

## Dependencies & Installation
This project uses Selenium (3.141.0), in particular its Chrome Webdriver. The script was built to work with Python 3.5+. While the script may work with Python 2.7, support is not guaranteed in present or future versions. 
<br/><br/>First of all, install pip (pip3) if you haven't already! You can learn more here: https://stackoverflow.com/a/6587528
<br/><br/>To install Selenium via pip3, run the following commands on your terminal:
<pre>$ pip3 install selenium</pre>
To upgrade Selenium to the latest version:
<pre>$ pip3 install --upgrade selenium</pre>
You may have to use superuser mode to install Selenium. For example:
<pre>$ sudo -H pip3 install selenium</pre>

## Usage
After setting up the dependencies, run the mainScript.py. 
<br/><br/>
<strong>Step 1:</strong> Choose which result you want to check.
<br/><br/>
<strong>Step 2:</strong> Enter the targeted school number and centre number.
<br/><br/>
<strong>Step 3:</strong> Enter the student-specific details (student's initial and mother's initial), whichever ones you know. If you don't know any one or both, they will be bruteforced with a loop on an alphabet dictionary.
<br/><br/>
<strong>Step 4:</strong> If known, enter the student's roll number. Else, enter a range to test against with a loop.
<br/><br/>
<em>NOTE: Not knowing the above three credentials will usually create time-consuming nested loops which might even provide unexpected results of students other than the targeted one. </em>

## License
This is free software released into the public domain. Anyone is free to copy, modify, use, compile, or distribute this software, either in source code form or as a compiled binary, for any non-commercial purpose, by any means that is not harmful to the audience it is targeted upon.

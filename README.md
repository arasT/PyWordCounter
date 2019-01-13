PyWordCounter
=========

Python script to display the number of lines, words and characters for a text file or a website. And a table about number of each word is displayed and can be saved into a csv file.
Please check [PyWordCounterGUI](https://github.com/arasT/PyWordCounterGUI) if you want to use GUI interface instead of console script.

Screenshots
---
<img src="./screenshots/pywc_result.png" alt="PyWordCounter result a text file" width="800">
<img src="./screenshots/pywc_url.png" alt="PyWordCounter result from website" width="800">
<img src="./screenshots/pywc_csv-result.png" alt="PyWordCounter  csv result" width="800">

How to use
---

This app is developped in [Python2.7](https://www.python.org/download/releases/2.7/).

Clone or Download this repository.
```
git clone https://github.com/arasT/PyWordCounter
```
Extract the archive and move into it.
```
cd PyWordCounter
```

Run
---
The minimal way to launch the script is to run the main script and indicate a text file.
```
python main.py -i lorem.txt
```
Or indicating a website url.
```
python main.py -u https://www.lipsum.com/
```
For example: Display words having more than one character and appears more than five times.
  Then save result into csv file.
```
python main.py -i lorem.txt -l 1 -n 5 -o lorem.csv
```
See more options by displaying help.
```
python main.py -h
```

License
----

The MIT License.
Further details see LICENSE file.


Contributing
----

Please fork if you want to contribut to this project.

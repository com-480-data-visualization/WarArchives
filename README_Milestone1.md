# Milestone 1

| Student's name | SCIPER |
| -------------- | ------ |
| Jaime Oliver Pastor| 356574|
| Alexandre Majchrzak| 345483|
| Antony Picard| 332025| |


### Dataset

The datasets we will be using were found on Kaggle, and are subsections of the THOR database. This database consists of a large amount of data on bombings from WW1 to the Vietnam War. It is very difficult to compile completely, and it is very large, so we have secured the ones that were freely available on Kaggle. These are the ones on WW1, WW2, the Korean War and the Vietnam War.

### Problematic

We want to show with our visualisation how bombings were used to attempt to win wars, did they become strategically important, was the bombload larger later on? All of this will be extracted from the dataset in which we can analyse the bombload by country over time and how many planes carried it. We can also see where they were dropped (not for the Korean War) and sometimes we can see a bit more depending on which of the four datasets.

### Exploratory Data Analysis

We have processed the data using panda, in python. This is done in the python files called DataProcessor, DataSplitter and DataAnalyser, most of the code is standard and pretty common. We have removed all lines that were missing crucial information, we have removed all duplicates and we have removed all columns that did not interess us, such as the model of aircraft used to carry the bomb for example, as it is interesting but irrelevant to our visualisation and objectives.
The next file was used to split a very large resulting database on the Vietnam War into multiple smaller files, as they were too large to upload to Github on their own, this is also why the only missing raw data file is the Vietnam War one, as it was too large.
The last does a small analysis on the current data, mostly what the average bombload was, and what the total bombload was, we can already see it became larger over time, as more bombings were used to avoid sending ground troops.

### Related work

Similar work has been done with History data in general, it is often very large and difficult to represent, so a standard representation on a map is often used. However, when it comes to bombings and their development, we have usually seen simpler graphs that simply show how the amount increased, and usually throughout a war instead of throughout multiple wars. Additionally, the amount of information we attempt to show is much greater than usual, as it is more specific and large scale visualisations don't exist.
A good example of something that inspired the work is WW2 Bombing Maps on Kaggle, which shows how to display on the map where the bombings were, we want to focus on a much larger time scale as well as on the amount of bombs, not just the place, so it is different, but it was definately an inspiration.


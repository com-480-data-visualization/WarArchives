# Project of Data Visualization (COM-480)

| Student's name | SCIPER |
| -------------- | ------ |
| Jaime Oliver Pastor| 356574|
| Alexandre Majchrzak| 345483|
| Antony Picard| 332025|

## Setup Instructions

- Clone or download the GitHub project.

- Open a terminal in the project root, where `index.html` and `DataAggregator.py` are located.

- Make sure Python is installed or install it if it isn't:

- Install the required pandas Python package (this is used for the processing of the data):

  ```bash
  pip install pandas
  ```

- Make sure the processed CSV files are in the expected folder structure:

  ```text
  Data/Processed/
  ├── ww1_processed.csv
  ├── ww2_processed.csv
  ├── korea_processed.csv
  ├── vietnam_part_1.csv
  ├── vietnam_part_2.csv
  ├── ...
  └── vietnam_part_10.csv
  ```

- Run the data aggregation script to generate the files needed for the website:

  ```bash
  python3 DataAggregator.py
  ```

  On Windows:

  ```bash
  python DataAggregator.py
  ```

- This should create the following files in the `data/` folder:

  ```text
  data/
  ├── timeline.json
  ├── map_data.json
  ├── stats.json
  ├── top_targets.json
  ├── by_country.json
  └── top_aircraft.json
  ```

- Start a local web server from the project root:

  ```bash
  python3 -m http.server 8000
  ```

  On Windows:

  ```bash
  python -m http.server 8000
  ```

- Open the visualisation in a browser:

  ```text
  http://localhost:8000
  ```

## Description

The website has a narrative structure, meant to jump at you, the first thing you see is the heatmap of the places bombed for all conflicts joined together, but one can scroll down to see the other graphs, including the missions over time, the attacking countries, the type of aircraft, and the bombed locations. All of these can be accessed by both scrolling and also by the menu on top. Also, in order to ensure exploration is possible, we have allowed in every graph and visualisation, alternatives for displaying, usually reducing the amount of wars displayed, chosing only one, or even changing the scale in a graph.

## Screencast

It is also important to know that the screencast is in the releases section, there is a release called WarArchives Video, which includes the mp4 so that it can be watched.
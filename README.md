# cintel-05-cintel
# Module CC5.2: Use a Python Deque

## Overview
This project demonstrates the use of the Python `collections.deque` data structure to efficiently manage and analyze recent data points in a live data stream. Deques allow adding and removing items from both ends, making them ideal for sliding window analytics on streaming data.

## What I Learned
- The `deque` class is part of the Python Standard Library (`collections` module), so it requires no extra installation.
- Deques can be initialized empty or with existing lists.
- Items can be appended to the right (newest) or left (oldest) end.
- Items can be removed from the right or left using `pop()` and `popleft()`.
- Using the `maxlen` parameter limits the deque size, automatically discarding the oldest data when new items are appended beyond the max length.
- These features make `deque` perfect for continuous intelligence and real-time analytics on streaming data.

## How I Implemented It
- Created empty and pre-filled deques representing temperature readings in Fahrenheit and Celsius.
- Practiced appending new data points and removing old ones.
- Used the `len()` function to get the current size of the deque.
- Cleared a deque to reset data for a new cycle.
- Simulated a live stream of Microsoft stock prices with a max length deque, showing automatic removal of the oldest prices when new ones come in.

## Running the Code
Run the `dashboard/app.py` file using Python in your terminal:

```bash
python dashboard/app.py
```


## Interactive App with Continuous Intelligence

This project demonstrates a live dashboard built with PyShiny Express that updates continuously with simulated real-time data. It showcases key concepts of continuous intelligence by displaying live values, a live data grid, and an interactive chart with a trend line prediction.

---

## Features

- Simulates live temperature readings updated every second
- Uses a reactive `deque` to store recent data points
- Displays current temperature and timestamp in value boxes
- Shows recent readings in a live data table
- Interactive Plotly scatter plot with a regression trend line
- Simple, clean UI with a sidebar for navigation and links

---

## Project Structure

- `dashboard/app.py`: Main app script with UI and reactive logic
- `README.md`: This documentation file
- `.gitignore`: Git ignore rules
- `requirements.txt`: Project dependencies

---

## Setup and Running Locally

1. Clone the repo:
```bash
https://github.com/teflxndxn/cintel-05-cintel.git 
```

2. Create and activate a Python virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run the app:
```bash
shiny run --reload --launch-browser dashboard/app.py
```
5. Open the browser if not opened automatically at `http://127.0.0.1:8000/`

---

## Customization and Enhancements

- Theme and layout can be changed to better suit your domain
- Replace simulated temperature data with your own live data source
- Extend charts to reduce flashing on updates or add more analytics
- Integrate this continuous intelligence app into other projects

---

## Author

Blessing

---




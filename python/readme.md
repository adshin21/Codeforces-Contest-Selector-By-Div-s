# Codeforces Contest Selector

This project fetches a list of contests from the Codeforces API, filters them based on specific criteria (Div. 3 and Educational contests), and saves the results to text files.

## Prerequisites

- Python 3.x installed on your system

## Installation

1. Clone the repository or download the `cf.py` file to your local machine.

2. Ensure you have Python 3.x installed. You can check your Python version by running:

```sh
python3 --version
```

## Running the Script

1. Open a terminal and navigate to the directory where `cf.py` is located.

2. Run the script using Python 3:
    ```sh
    python3 cf.py
    ```

## Output

The script will create two text files in the same directory:

- `Div3.txt`: Contains the list of Div. 3 contests.
- `Educational.txt`: Contains the list of Educational contests.

## Notes

- Ensure you have a stable internet connection as the script fetches data from an external API.
- If the API request fails, the script will log an error message and suggest trying again after a few minutes.

## Example Output

- `Div3.txt`

  ```
  Div3 Rounds 1 :  http://codeforces.com/contest/1234
  Div3 Rounds 2 :  http://codeforces.com/contest/5678
  ```

- `Educational.txt`
  ```
  Educational Round 1 :  http://codeforces.com/contest/91011
  Educational Round 2 :  http://codeforces.com/contest/121314
  ```

## Troubleshooting

- If you encounter any issues, ensure that you have Node.js installed correctly and that you have an active internet connection.
- Check the console output for any error messages that might indicate what went wrong.

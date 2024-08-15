# Codeforces Contest Fetcher

This script fetches the list of contests from Codeforces and categorizes them into "Educational" and "Div. 3" contests. It then writes the contest details into separate text files.

## Prerequisites

- Node.js installed on your machine.
- Internet connection to fetch data from Codeforces API.

## Installation

1. Clone the repository or download the script file `cf.js`

2. Navigate to the directory containing the script.

```sh
cd path/to/your/directory
```

3. Install the required Node.js modules. This script uses the `fs` and `fetch` modules which are built-in with Node.js, so no additional packages are required.

## Usage

1. Run the script using Node.js.

```sh
node cf.js
```

2. The script will fetch the contest data from Codeforces and create two text files in the same directory:
   - `Div3.txt`for Div. 3 contests.
   - `Educational.txt` for Educational contests.

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

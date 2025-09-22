## 📌 Task
Implement a program that:  

1. Expects the user to specify as a **command-line argument** the number of Bitcoins `n` they would like to buy.  
   - If the argument cannot be converted to a `float`, exit with `sys.exit` and an error message.  
2. Queries the API for the **CoinCap Bitcoin Price Index** at:  
   (``.)
   https://rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey
   (``.)  
   Replace `YourApiKey` with your actual CoinCap API key.  
   - The response is a JSON object containing the **current price of Bitcoin** as a float.  
   - Catch all exceptions with `try/except requests.RequestException`.  
3. Outputs the **current cost** of `n` Bitcoins in **USD**, formatted with:  
   - Four decimal places.  
   - `,` as a thousands separator.  

---

## ⚙️ Requirements
- Use `sys.argv` to read the command-line argument.  
- Validate and convert input to a `float`.  
- Use the `requests` library to fetch JSON from the API.  
- Extract Bitcoin’s current price from the nested JSON structure.  
- Format output with `f"{value:,.4f}"`.  
- Handle errors gracefully (invalid input, request failure, etc.).  

---

## 💡 Hint
- Example structure for validation:  
  (``.)python
  import sys
  if len(sys.argv) != 2:
      sys.exit("Missing command-line argument")
  try:
      n = float(sys.argv[1])
  except ValueError:
      sys.exit("Command-line argument is not a number")
  (``.)  
- Example for requests:  
  (``.)python
  import requests
  try:
      response = requests.get(url)
      data = response.json()
  except requests.RequestException:
      sys.exit("Request failed")
  (``.)  
- Extract Bitcoin price from JSON (check API docs for exact structure).  

---

## 💻 Solution
👉 [bitcoin.py](bitcoin.py)

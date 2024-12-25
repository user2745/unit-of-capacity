---

# **Generic Unit of Capability**

---

## **Overview**
This project demonstrates a generic Unit of Capability, designed to process and transform data in a meaningful way. The unit consists of three core components:
1. **Data Ingestion**: Fetches raw data from a specified endpoint.
2. **Processing**: Transforms the data into a usable format.
3. **Logging**: Outputs the processed data for review or further use.

---

## **Features**
- Fetches live data from an API.
- Processes data to round numeric values for clarity.
- Logs the processed data for validation.

---

## **How to Run**
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Start the script:
   ```
   python main.py
   ```

---

## **Example Output**
When executed, the program outputs:
```
Fetched Data: {'cpu': 70.12345, 'memory': 50.98765, 'disk': 30.54321}
Processed Data: {'cpu': 70.12, 'memory': 50.99, 'disk': 30.54}
Logged Data: {'cpu': 70.12, 'memory': 50.99, 'disk': 30.54}
```

---

## **Structure**
- **`main.py`**: Orchestrates the Unit of Capability.
- **`modules/`**:
  - **`data_ingestion.py`**: Fetches raw data from an endpoint.
  - **`processing.py`**: Processes raw data to round numeric values.
  - **`logging.py`**: Logs processed data.

---

## **Future Enhancements**
- Add support for nested data structures.
- Enable real-time data updates.
- Implement advanced logging mechanisms.

---

Let me know if this works or needs adjustments! 🚀
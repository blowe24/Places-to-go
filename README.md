# Places-to-go
**CLI app built with python and postgresql to track places to go such as restaurants**

- This CLI app connects to a local postgresql server to store the data
- Running this app it will first prompt with the option to ADD or LOOKUP
1. ADD - takes input of country, city, and name. I chose city as that is universal through out different countries. Each entry will also be assigned also be assigned a unique ID. 
2. LOOKUP - asks if user wants ALL, country, city, or name outputs. Once selected it will query them from the restaurant table and return them back.
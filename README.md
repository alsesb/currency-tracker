# Currency tracking with thread pool
Small python script to watch your currency rates.

### API Key:
- Check https://www.abstractapi.com/ for api key

### How-to:
1. Create an account for abstract api
2. Select the exchange rates from the left menu
3. Copy your private api key from the site
4. Download the code (if you haven't already)
5. Create a copy of .env.example and rename it to .env
6. Paste your private api key to API_KEY=YOUR_API_KEY
7. Set a timeout (in seconds) between separate calls e.g. CALL_TIMEOUT=60
8. Set the number of threads allowed in the pool (number separate base currencies you would like to watch) e.g. THREAD_POOL=10

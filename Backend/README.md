# Local Development
1. Open terminal or command prompt.
2. Check which version of Python your computer has by executing
   ```
   python --version
   ```
   If it shows Python 3, continue to step 2. Otherwise, try executing 
   
   ```
   python3 --version
   ```
   If it shows Python 3, substitute all `python` commands below with `python3`.
   
   Otherwise, install Python 3.
3. Create virtual environment in this directory by executing
   ```
   python -m venv env
   ```
4. Activate virtual environment by executing
   ```
   source env/bin/activate
   ```
5. Install all required modules by executing
   ```
   pip install -r requirements.txt
   ```
6. Run localhost server by executing
   ```
   python app.py
   ```
7. Make sure your localhost server works. Open `http://0.0.0.0:5000` in any browser. If there is no problem, it should display
   ```
   { "root": true }
   ```
7. If you are done, turn off your localhost server by pressing `ctrl + C`.
8. Deactivate your virtual environment by executing
   ```
   deactivate
   ```

# Deployment
You can access the deployment server in this [link](https://backend-bangkit-jkt-1-e.herokuapp.com/)
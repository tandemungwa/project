<b> NOTE</b>: This was made on Windows 10.

<h1> Dependencies </h1>

First, clone the project into a folder using <code>git clone</code>.

Prior to running scripts, setup the following Conda environment: 

Create conda environemnt with (specifically) Python 3 
<br/>
<code> conda create -n myenv python=3 </code>
<br/>

Activate conda environment
<br/>
<code> conda activate myenv </code>
<br/>

Install pandas in conda environment
<br/>
<code>conda install -c anaconda pandas</code>
<br/>

Install requests in conda environment
<br/>
<code> conda install -c anaconda requests  </code>
<br/>

Add conda-forge channel, then install prettytable in conda environment
<br/>
<code> conda config --add channels conda-forge </code>
<br/>
<code> conda install prettytable </code>

<br/>
<h1> Database </h1>
For a database, I used <code>sqlite3</code> in python, which creates a <code>.db</code> file which is queried from the python code with standard SQL commands. This removes the need for an external database client. 
<br/>

<br/>
<h1> Running Scripts </h1>

Run <code> python main.py</code> and observe results in the terminal.
<br/>

On the first run, the script will:
1. Scrape data from <a href="https://www.themoviedb.org/?language=en-US">TMDb API</a>
2. Save data into <code>data.csv</code>
3. Start and connect to sqlite database <code>database.db</code>, which is stored locally
4. Populate <code>database.db</code> tables with data from <code>data.csv</code>
5. Run queries. 
  
On subsequent runs, because <code>data.csv</code> and <code>database.db</code> already exist, 1-4 are effectively skipped, and the queries will run. This allows you to modify the queries and get the results without having to wait for the API calls & for the SQL table to populate. 

To reset the program, run reset.py, which deletes <code>data.csv</code> and <code>database.db</code>, forcing the program to begin from step 1. 

<b>NOTE</b>: The queries use PrettyTable to print neat tables in the terminal, make sure the terminal window is wide enough or the tables will not display properly.




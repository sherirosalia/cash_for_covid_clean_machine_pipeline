# PPP_Covid_Stimulus

### PPP loans - stimulus money exploration
This project aims to explore and analyze the "Paycheck Protection Program" loan data recently released by the Small Business Association.  Otherwise known as "PPP", these potentially forgivable loans are part of the Covid relief package authored by the US Government in an attempt to assist businesses to retain employees and "stay in business". 

### The data 
Over 4 million rows of data resulted from a compilation of the 51 CSV files that the US Treasury made public  <a href='https://home.treasury.gov/policy-issues/cares-act/assistance-for-small-businesses/sba-paycheck-protection-program-loan-level-data'><strong>available</strong></a>. 50 CSV files have state specific, anonymized information about loans up to 150k. The one remaining CSV is nationwide and reveals the identities of the borrowers of larger loans that go into the millions.

### The approach
Python was used to join the 50 state CSV files and Python Pandas to clean and normalize the data. Taking advantage of the extra horsepower afforded by Google Colab, a preliminary analysis and export of the tightest data (people_ppp.csv) was done using PySpark. Workbooks and scripts are in this repository.

### Analysis
Currently in process, but a few visualizations for the State of California and the one Nationwide CSV file are in Tableau Public. These were done before combining all of the state data. 

Next steps are to run the people_ppp.csv which as of now is about 300k rows through a machine learning package or two and do a deeper dive into the entire dataset which even after munging is about 4 million rows and looks promising.

Even at this light stage of analysis, there have been some insights gleaned. 
- The largest lenders are for the most part "brick and mortar", household names such as Wells Fargo and Bank of America, but there are a few Fintech companies that made the top 10 such as PayPal and Square. 
- The median loan amount was roughly the same as the average for women namely 34k, but male owned businesses borrowed 41k and Veterans the lowest average amount at about 21k. 
- Amongst racial groupings, based on those who responded, the number of Asians who borrowed was double the count of Hispanics despite being a smaller percentage of the population. 

Of course there are many potential pitfalls to the above. For example, most borrowers declined to state their race, gender and military service status, so the figures above are based only on respondents who answered and this could inaccurately skew results. 

### Tableau Public
Tableau Public link is here:  <a href='https://public.tableau.com/profile/cerejarosinha#!/vizhome/ppp_loan_analysis/LoansbyLender?publish=yes'><strong>PPP Loan Maps and Preliminary Analysis</strong></a>.

### Frameworks
- Python Pandas
- Tableau
- PySpark
- Python

### Folder Structure
Root:
- Readme.md
- Screenshot of map visualization
Tableau:
- Tableau Desktop (.twbx ) includes a data extract.
pandas_csv_cleaning:
- Transformation pipline contained in a series of notebooks.
python_csv
- Python script enabling union of the loan data csv files for individual states from Small Business Administration.
pyspark_analysis:
- Preliminary exploration of the cleaned data and production of people_ppp.csv file.

### Deployment
- Download the files from the US Treasury linked above, deploy the script in "python_csv" and then run the resulting CSV file through "clean.ipynb" in the "pandas_csv_cleaning" folder. Notes indicate which notebooks to run sequentially. 
- PySpark script utilizes CSV file exported in clean_ppp3.ipynb.

### California map analysis - top lenders
![](PPP_stimulus_california.png)


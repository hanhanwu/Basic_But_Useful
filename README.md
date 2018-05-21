# Basic_But_Useful


* Python write .csv with a list of records: https://github.com/hanhanwu/Basic_But_Useful/blob/master/python_write_csv_iterate.py

* Create SQL Server Job and call SSIS package to import periodically data automatically
  * Add SQL Server Agent if you don't have one, with SQL Server Agent, you will be able to create jobs: https://technet.microsoft.com/en-us/library/ms187901(v=sql.110).aspx
  * Create a SQL Server Job: http://www.codeproject.com/Tips/620768/Create-New-Jobs-In-SQL
  * Create a SSIS package for data import: http://stackoverflow.com/questions/39028577/import-large-flat-file-with-very-long-string-as-ssis-package
  * Run SSIS Package through a Job: http://www.sqlshack.com/ways-use-execute-sql-server-integration-services-packages/
  * <b>NOTE</b>: Simply create an SSIS package could only import 1 file. I tried <b>SSIS Froeach Loop Editor</b> and <b> SQL Server Stored Procedure</b> for multiple files data import.
  * Import data through Stored Procedure: http://stackoverflow.com/questions/16076309/import-multiple-csv-files-to-sql-server-from-a-folder
  * SSIS foreach loop editor: https://www.mssqltips.com/sqlservertip/2874/loop-through-flat-files-in-sql-server-integration-services/
  * Configure SSIS foreach loop editor: https://msdn.microsoft.com/en-us/library/ms140016.aspx
  * Download SSIS foreach loop editor: https://msdn.microsoft.com/en-us/mt186501
  * SSIS Major Tutorial: https://msdn.microsoft.com/library/ms169917.aspx
  * Using SSIS Foreach Loop Editor: https://msdn.microsoft.com/en-us/library/ms169800.aspx
  * Allow SSIS Foreach Loop Editor to choose the new file each time: http://stackoverflow.com/questions/6913499/how-to-change-flat-file-source-using-foreach-loop-container-in-an-ssis-package
 
* <b>SUMMARY</b>: Import multiple data with SSIS Foreach Loop Editor
  * I failed several times, finally got it right. You may not succeed by simply checking MSDN tutorial
  * Step 1: Download and install SSDT (SQL Server Data Tools) for your Visual Studio, 2015 is the best version. After the installation, instead of start Visual Studio, fid "SQL Server Data Tools" through Start program on Windows. It has a visual studio logo.
  * Step 2: Create an Integration Services Project like this: https://msdn.microsoft.com/en-us/library/ms170057.aspx
  * Step 3: Create a new package. Then, drag <b>Foreach Loop Container</b> from <b>Containers</b> in <b>SSIS Toolbox</b>
  * Step 4: Double Click <b>Foreach Loop Container</b>, in <b>Foreach Loop Editor</b>, click <b>Variable Mappings</b>, add a new Variable (Name=RootFolder, Value=[your soure folder path]), add another Vaariable (Name=FilePattern, Value=[the common prefix in import data file names, such as "transaction_data"]).
  * Step 5: Click <b>Collection</b>, click <b>...</b> in Expression, add 1 <b>Directory</b> as property, the drag @[User::RootFolder] as value, you can click <b>Evaluate Value</b> to check, this is the folder path. add <b>FileSpec</b> as another property, drag @[User::FilePattern] as the value, this is the pattern of your file name, if you file name will change when time changes, check the solution here as reference: http://stackoverflow.com/questions/6913499/how-to-change-flat-file-source-using-foreach-loop-container-in-an-ssis-package
  * Step 6: After clicked OKs in the last step and closed the Foreach Loop Editor, drag <b>Data Flow Task</b> from Favorites in SSIS Toolbox. Double click data flow task. In<b>Connection Managers</b>, drag <b>Flat File Source</b> to define a sample data source, all the other data import files will follow the same rules set in this sample file to be imported. Drag <b>OLE DB Destination</b> in the Connection Managers too, define where you want to store the imported data.
  * Step 7: Drag <b>Flat File Source</b> from SSIS Toolbox onto <b>Data Flow</b> surface, double click it and choose your source in Connection Managers
  * Step 8: Drag <b>OLD DB Destination</b> from SSIS Toolbox to Data Flow surface too, link the Flat File Source to it, then double click on it and add your destination from Connection Managers, the table name may need to define from the query if it's a new table
  * Step 9: Execute this whole package should be able to work.
  * Step 10: If the file names may change, simply modify the FilePattern in Foreach Loop Container.
  * Step 11: If you want this package to be executed periodically, create a SQL Server job and execute the package, check this link: http://www.sqlshack.com/ways-use-execute-sql-server-integration-services-packages/


* SQL Server Agent
  * How to allow SQL Server job sends notifications to a specific non-DBA email: https://www.mssqltips.com/sqlservertip/1523/how-to-setup-sql-server-alerts-and-email-operator-notifications/

* R Seperate Data Columns based on Data Types
  * Extract all factor columns from the original: https://github.com/hanhanwu/Basic_But_Useful/blob/master/extract_all_factor_columns.R
 
 
* R Basics
  * R functions have different names as other programming languages, but server for the same purpose:
  https://github.com/hanhanwu/Basic_But_Useful/blob/master/R_functions.R
  * Data Preprocessing part 1: https://github.com/hanhanwu/Basic_But_Useful/blob/master/R_data_preprocessing_1.R
  * When I was doing data cleaning, generated a SRAT WAR DISTRIBUTION by accident :) What a perfect normal distribution :) https://github.com/hanhanwu/Basic_But_Useful/blob/master/star_war_distribution.PNG
  * In R, the default setting for boxplot is to extend whiskers 1.5*IQR higher than Q3 and lower then Q1, which helps a lot for finding potential outliers
  * How to deal with 0 standard deviation in R: https://github.com/hanhanwu/Basic_But_Useful/blob/master/deal_with_zero_variance.R
  * When converting skewed data into normal distribution, sometimes need to try both `log()` and `sqrt()` and see which result is closer to normal distribution
  * When using R newest verision Random Forest, especially the one in mlr, there are something to note (check comments in my code): https://github.com/hanhanwu/Basic_But_Useful/blob/master/mlr_random_forest.R
  * It seems that R Random Forest can no longer handle ordereed Factor variable, and therefore, factor variables need to be converted into numerical data. But if your predict.type is "response", the label still has to be Factor variable: http://stackoverflow.com/questions/17352324/new-factor-levels-not-present-in-the-training-data
  * When checking the confusion matrix output as my code above, it's better to use <b>Balanced Accuracy</b> instead of Accuracy: http://ong-home.my/papers/brodersen10post-balacc.pdf
  * With mlr package, we can get feature importance easier by chosing which method do we need, such as Random Forest or Information Gain, it also allows you to tune the parameter of these methods: https://github.com/hanhanwu/Basic_But_Useful/blob/master/mlr_feature_importance.R
  * mlr find learners: https://github.com/hanhanwu/Basic_But_Useful/blob/master/mlr_find_learners.R
  * mlr package (page 32 is about feture importance): https://cran.r-project.org/web/packages/mlr/mlr.pdf 
  * R data.table basics: https://github.com/hanhanwu/Hanhan_Data_Science_Practice/blob/master/R_data.table_basics.R
  * data table group by and select count, max: https://github.com/hanhanwu/Basic_But_Useful/blob/master/R_group_by.R
  * reduce levels when the levels is a large number: https://github.com/hanhanwu/Basic_But_Useful/blob/master/reduce_large_levels.R
 * ASCII and Binary characters: http://roubaixinteractive.com/PlayGround/Binary_Conversion/The_Characters.asp
   * Example: Type `print chr(119)` in python terminal, the special character will be output


* PowerBI Automation
  * Text analysis will be done in Python on local machine
  * To schedule automatically running python code periodically
 
  1. http://gis.stackexchange.com/questions/140110/running-python-script-in-task-scheduler-script-will-not-run
  2. https://blogs.esri.com/esri/arcgis/2013/07/30/scheduling-a-scrip/
   
  * PowerBI connects to OneDrive for auto refresh seems have more flexibility
 
  1. PowerBI data refresh: https://powerbi.microsoft.com/en-us/documentation/powerbi-refresh-data/
  2. The python output should be .csv format, and the output will be sent to OneDrive, so that PowerBI could read the file: https://github.com/OneDrive/onedrive-sdk-python
  3. (Optional) If have to use on-premise SQL Server (but needs to download and install PowerBI gateway, not sure whether it's for Pro only or not), here is how Python connects to SQL Server: http://stackoverflow.com/questions/25754083/sql-server-query-with-python
  4. NOTE1: Use MSFT Application Registration Portal to create your OneDrive API keys and secrets
  5. NOTE2: In step 2 above, when I am trying to get the authentication code after pasting the auth_url to my browser, I have to login my own Microsoft account, even though I created this OneDrive app with my company account. (I know, MSFT never make your life easier)
  6. NOTE3: Similar to LinkedIn authentication method, the code you got here will expire within seconds

  * Putting data in cloud such as OneDrive, some companies which have very high security settings may have concern about this, therefore, having personal PowerBI Gateway installed may make them feel better.... But the gateway is for PowerBI Pro only: https://powerbi.microsoft.com/en-us/documentation/powerbi-personal-gateway/


* Python Basics
  * Python Basics: https://github.com/hanhanwu/Basic_But_Useful/blob/master/python_basics.py
  * Python Random Search vs Grid Search
    * My code: https://github.com/hanhanwu/Basic_But_Useful/blob/master/RandomSearch_vs_GridSearch_cv.ipynb
      * sklearn Random Search
      * sklearn Grid Search
      * Hyperopt (random search)
      * In the code, Hyperopt can find the best model with optimized params while sklearn needs to specify a model such as random forests, but sklearn is much faster.
      * Both sklearn and hyperopt methods have cross validation settings
    * More about Hyperopt
      * To check which param you can tune: https://github.com/hyperopt/hyperopt-sklearn/blob/master/hpsklearn/components.py
      * To check all the supported classifers, regressors, etc., check: https://github.com/hyperopt/hyperopt-sklearn
      * If you got error `TypeError: 'generator' object has no attribute 'getitem'`
        * `pip search networkx|grep networkx`, check whether you have networkx 2.0+
        * If so, type `sudo pip install networkx==1.11`
    * Previously, I tried `TPOT`, it can also find the best model with optimized params
      * My code: https://github.com/hanhanwu/Hanhan_Data_Science_Practice/blob/master/try_genetic_alg_through_TPOT.ipynb
  * When adding dictionary in python list, use `copy()`, otherwise its the reference has been appended: https://github.com/hanhanwu/Basic_But_Useful/blob/master/note_python_list.py
  * A flexible way to strip the html tags, you can modify the function to cater for specific use, works for both Python 2.7 and Python 3.*: https://github.com/hanhanwu/Basic_But_Useful/blob/master/strip_html_tag_python.py
  * Features from 3.* can be used in Python 2.7: https://docs.python.org/2/library/__future__.html
  * After you finally have install a python package, but when you try to import, it is showing "Permisson Denied [path]", try this commend line in your terminal `sudo chown -R $USER /Library/Python/2.7/site-packages/`, in my case, the installed package is in site-packages folder. `chown` means change the user permission for a folder/file. 
  * Different ways to deal with unicode in Python: https://github.com/hanhanwu/Basic_But_Useful/blob/master/about_unicode.py
  * Python read multi-format files (it can read PDF, DOCX, MP4): https://www.analyticsvidhya.com/blog/2017/03/read-commonly-used-formats-using-python/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29
  * Many datasets use X, Y system instead of latitude, longitude, therefore, tools like Tableau could not recognize the data on its map. Here, I am using a simple way to convert X, Y to latitude and longitude (need to check DATUM and projection of the region first): https://github.com/hanhanwu/Basic_But_Useful/blob/master/XY_to_latitude_longitude.py
  * Python UnitTest introduction example: http://pythontesting.net/framework/unittest/unittest-introduction/
  * Python argparse is a good tool to allow you define command line input parameters, because python built-in parameters are limited. In my code example, just go to the folder of this source code, run command line through terminal `pydoc3 test_arg.TestArg.get_arguments`, here is my code for reading the command line parameters: https://github.com/hanhanwu/Basic_But_Useful/blob/master/python_argparse.py
 * Python dictionary is randomly ordered
   * My code: https://github.com/hanhanwu/Basic_But_Useful/blob/master/python_dct_and_order.py
     * arrange keys in a dictionary in order
     * make a dictionary arranged in key order
* Python Excel: https://github.com/hanhanwu/Basic_But_Useful/blob/master/python_excel.py
* `seaborn` - an easy-to-use python visualization
  * my code: https://github.com/hanhanwu/Basic_But_Useful/blob/master/python_distribution_visualization.ipynb
  * The visualization here is majorly for distribution analysis (univariate, bivariate)
  * By default, `kdeplot()` is using "gaussian" as kernel type, so when you are giving an array of numbers, it converts to gaussian distribution like curves
* Other Python Visualization: https://github.com/hanhanwu/Basic_But_Useful/blob/master/python_visualization.py
* Python Pandas
  * I'm updating pandas and python dataframe here too: https://github.com/hanhanwu/Basic_But_Useful/blob/master/python_dataframe.py
  * My pandas code: https://github.com/hanhanwu/Hanhan_Data_Science_Practice/blob/master/try_pandas.ipynb
  * My pandas used in biclustering code: https://github.com/hanhanwu/Hanhan_Data_Science_Practice/blob/master/HiCS_biclustering.ipynb
  * My pandas code used in preprocessing here: https://github.com/hanhanwu/Hanhan_Data_Science_Practice/blob/master/try_lightfGBM_cv.ipynb
  * Pandas code here: https://github.com/hanhanwu/Hanhan_Data_Science_Practice/blob/master/deal_with_data_shifting.ipynb
    * Note: for label encoding here, it does label encoding for training and testing data seperately, may not be a good way. Better to combine training and testing data first, and do label encoding together
  * Pandas code here: https://github.com/hanhanwu/Hanhan_Data_Science_Practice/blob/master/try_genetic_alg_through_TPOT.ipynb
    * Resolved the label encoding problem appeared above
  * Pandas code: https://github.com/hanhanwu/Hanhan_Data_Science_Practice/blob/master/AI_Experiments/try_audio_deep_learning.ipynb
* Statistics Basics in Python: https://github.com/hanhanwu/Basic_But_Useful/blob/master/statistics_python_basics.py
* Read image url and open image: https://github.com/hanhanwu/Basic_But_Useful/blob/master/python_read_image_url.ipynb
  * I love flowers!
* Python download images: https://github.com/hanhanwu/Basic_But_Useful/blob/master/python_download_images.ipynb
  * NOTE: If the image does not exists, but there is another image such as empty image there, will still be downloaded
* Latitude, longitude to location: https://github.com/hanhanwu/Basic_But_Useful/blob/master/python_coordiates2location.ipynb
  * reference: https://chrisalbon.com/python/geocoding_and_reverse_geocoding.html
  * My 2016 post: https://stackoverflow.com/questions/35237426/geocoderserviceerror-for-geopy
    * The google map api worked in 2016, not it gives empty results. But the above method works at this moment (who knows when it will stop working too....), and it's just in simple lines
* Unequally Time Match
  * Sometimes, you need to match events that are not happen in the same time, but they are relevant. For example, in this code, there could be multiple oil analysis between 2 work order, and you want to find the latest oil analysis for each work order
  * code: https://github.com/hanhanwu/Basic_But_Useful/blob/master/time_match.ipynb
  
* Python FlashText - search & replace keywords faster than regex
  * https://github.com/hanhanwu/Basic_But_Useful/blob/master/try_flashtext.ipynb
* Python NLP commonly used basics operations
  * Basics 1 - https://github.com/hanhanwu/Basic_But_Useful/blob/master/NLP_basic_preprocessing.ipynb
  * Basics 2 - https://github.com/hanhanwu/Hanhan_Data_Science_Practice/blob/master/AI_Experiments/text_embedding_NN.ipynb
    * Only check Step 1 here. Very basics. Remove punctuation, only keep alphebic non-stop words with enough length. Finally remove those tokens with low occurance.
 

* PYTHON 3
  * How to have Python 3 without hurting 2.7: for me, I simply created a new project in PyCharm community Edition, and set the intepretor as python 3, just 1 seconds for this setting
  * Key difference between Python 2.x and Python 3.x: http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html
  * My test code with Python3: https://github.com/hanhanwu/Basic_But_Useful/blob/master/python3_test.py
 
 
* Visual Studio Free Version for Python is, stupid
  * Use Visual Studio Code (VSC) if Eclipse and PyCharm are not allowed to install in your company: https://code.visualstudio.com/docs/introvideos/overview?utm_expid=101350005-29.Dor1By5yTmynP2dmCMGGtw.1&start=true
  * VSC Python: https://code.visualstudio.com/docs/languages/python
  * VSC Basics: https://code.visualstudio.com/docs/editor/codebasics
 

* Change Between Python 2.x and 3.x
  * In some SDK such as Visual Studio Code, it doesn't allow you to use both types of Python at the same time with a flexibility, since it reads the Python version from Envirinment Variable. But some libraries you need are writtern in the Python version you don't use. change your Python version or change those code?
  * Download the right Python Version you want: https://www.python.org/downloads/
  * Edit System Environment Variable, add `C:\Python27;C:\Python27\Scripts;C:\Python27\Library\bin;` to PATH or replace Python 3 with this.


* Write and Append csv in python
  * code: https://github.com/hanhanwu/Basic_But_Useful/blob/master/write_csv.py
  * With python csv DictReader or DictWriter, even it's comma demilited and there are comma in the text of some columns, it can still recognize the right columns.
  * With this method, tools like PowerBI could recognize the right format, otherwise, even with .csv as the extension, it cannot load data right. What makes a difference is, whether you add 'b' in `open()` function


* Data Visualization
  * Python altair
    * It looks more pretty than `matplotlib`. But it doesn't support boxchart and other basics which matplotlib supports
    * Source: https://github.com/altair-viz/altair
    * Gallery: https://altair-viz.github.io/gallery/index.html#
    * my code: https://github.com/hanhanwu/Basic_But_Useful/blob/master/try_altair_visualization.ipynb
  * Tableau
    * Create distribution for a single column: https://www.interworks.com/blog/anonymous/2012/01/30/simple-histograms-tableau
    * Customize bins through query: http://reports4u.co.uk/tableau-create-bins-from-measure-calculation/
  * Excel
    * As a data scientist in modern world, are you going to use Excel? I will never choose that tool. Well, but in the workplace you are not working alone, sometimes, you have to work with those who uses Excel...
    * To get the chart from your excel data, select your data, and press `Alt + F1`
      * https://support.office.com/en-us/article/Create-a-chart-from-start-to-finish-0baf399e-dd61-4e18-8a73-b3fd5d5680c2
    * To change data labels, such change value to percentage, you need to select the chart, right click, if you are lucky, maybe able to see the right side tool bar to allow you click "Percentage"'
    * As for adding the legend, well, I really didn't find the good tutorial.... I copied other's legend. It seems that the legend used in that file matched to the wrong category, but used in my chart, it just right. So, it's lucky


* Perforce
  * Perforce Basics: https://github.com/hanhanwu/Basic_But_Useful/blob/master/perforce_basics.md

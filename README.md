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
 * Extreact all factor columns from the original: https://github.com/hanhanwu/Basic_But_Useful/blob/master/extract_all_factor_columns.R
 
 
* R Basics
 * Data Preprocessing part 1: https://github.com/hanhanwu/Basic_But_Useful/blob/master/R_data_preprocessing_1.R
 * When I was doing data cleaning, generated a SRAT WAR DISTRIBUTION by accident :) What a perfect normal distribution :) https://github.com/hanhanwu/Basic_But_Useful/blob/master/star_war_distribution.PNG
 * In R, the default setting for boxplot is to extend whiskers 1.5*IQR higher than Q3 and lower then Q1, which helps a lot for finding potential outliers


* PowerBI Automation
 * Text analysis will be done in Python on local machine
 * To schedule automatically running python code periodically
 
  1. http://gis.stackexchange.com/questions/140110/running-python-script-in-task-scheduler-script-will-not-run
  2. https://blogs.esri.com/esri/arcgis/2013/07/30/scheduling-a-scrip/
   
 * PowerBI connects to OneDrive for auto refresh seems have more flexibility
 
  1. PowerBI data refresh: https://powerbi.microsoft.com/en-us/documentation/powerbi-refresh-data/
  2. The python output should be .csv format, and the output will be sent to OneDrive, so that PowerBI could read the file: https://github.com/OneDrive/onedrive-sdk-python
  3. (Optional) If have to use on-premise SQL Server (but needs to download and install PowerBI gateway, not sure whether it's for Pro only or not), here is how Python connects to SQL Server: http://stackoverflow.com/questions/25754083/sql-server-query-with-python

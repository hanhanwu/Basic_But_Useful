My RA work finally has been finished on 2017/4/29. So excited and I have collected all the comand lines used in MAC/Linux terminal, GitHub commnds, as well as WestGrid (cloud) commnds. 
This file will also be used to record other commands.

***************************************************************************************

<b>Interact with Remote Linux Server</b>

* Remote login to school Linux server: `ssh [my school id]@rcg-linux-ts1.rcg.sfu.ca` 
* Download folder from school server to local machine: `scp -r [my school id]@rcg-linux-ts1.rcg.sfu.ca:/rcg/sentiment/SOC/Factiva_Data/Factiva_Articles/2016 [local folder path]/RA`
* Send local folder to school server: `scp -r [local folder path]/2016_more [my school id]@rcg-linux-ts1.rcg.sfu.ca:/rcg/sentiment/SOC/Factiva_Data/Factiva_Articles`
* `scp` when there is space in your path: `scp [my school id]@rcg-linux-ts1.rcg.sfu.ca:"/rcg/sentiment/SOC/OnlineData/GlobeAndMail/all_online_data/all_online_data\ 2/empty_comment_ids.txt"  [local path]`
  * In a word, when there is space in your path, add `""` around the path and use `\ ` to replace the space 


***************************************************************************************

<b>Mac/Linux Commnds</b>

* <b>NOTE:</b> If it is showing any error, try to start your commnd line with `sudo`, if your know admin id and password.
* List in files in time order: `ls -lt`
* List files with created time: `ls -ll`
* Copy file to another folder: `cp -r f1 [new_dir path]/f1`
* Count number of files in a folder: `find . -type f | wc -l`
* Find files start with (in this case, all start with 'article'): `find . -type f -name 'article*' | wc -l`
* Find files not start with (in this case, not start with 'article'): `find . -type f ! -name 'article*'`
* Count a specific word in all the files of a folder (in this case, count 'commentText'): `grep -roh commentText . | wc -w`
* Count line numbers in a file: `wc -l resources/seed_urls.txt`
* Zip dir: `zip -r ArticleRawData.zip ArticleRawData/`
* Unzip: `unzip manually_all_data.zip -d manually_all_data`
* Remove many files with same prefix (in this case, remove 'article_'): `find . -name 'article_*' | xargs rm`
* Find something in your machine with key words (in this case, find firefox): `mdfind firefox | grep 'firefox$'`
* Find running nohup job: `ps -ef | grep 'get_comment_reactions.py'`
* Kill running nohup job: `sudo kill -9 [job id]`, id is the last 4-digit number
* Use `nohup` or `screen` to run your code through the terminal, so that when you turn off the terminal, the code will keep running
  * Using `nohup` for python file: `sudo nohup python3.5 SFU_comments_extractor/source/ScrapeNews/get_comment_reactions.py`
  * Using `nohup` for .sh file: `sudo nohup sh run_news_scraper.sh`
  * Using `screen`: `sudo screen python3.5 SFU_comments_extractor/source/ScrapeNews/get_comment_reactions.py`
  * Personal, I prefer `nohup`, although it happened once when `nohup` didn't work but `screen` worked. `nohup` creates a log in the folder where you are running the `nohup` job, easier for debugging if necessary
* Add a library path to `$PATH`
  * export PATH=/Library/Frameworks/Python.framework/Versions/3.5/bin:$PATHf
  * export PATH=$PATH:/Users/devadmin/Documents/geckodriver
* `brew update` error
  * When you try commands like `brew update`, it may show you error: `Error: The /usr/local directory is not writable.`
  * To deal with this, type `sudo chown -R $(whoami):admin /usr/local`, here no need to change anything in the command
  * After that, change permission back by typing `sudo chown root:wheel /usr/local`
* Python Uninstall
  * `sudo easy_install -m [PACKAGE]`
  * `sudo rm -rf /usr/local/lib/python2.X/site-packages/[PACKAGE].egg` # remove egg file
* After installing xcode, if you get this error `error: tool 'xcodebuild' requires Xcode, but active developer directory '/Library/Developer/CommandLineTools' is a command line `
  * Type `sudo xcode-select -s /Applications/Xcode.app/Contents/Developer`
  * Then type `sudo xcodebuild -license`, type `agree` at the end of that license
* Mac SDK
  * To check all the SDKs provided by Apple: `xcodebuild -showsdks`
  * To check SDK on your own machine: `xcrun --show-sdk-path`
* Install conda on Mac
  * First of all, download and install conda .pkg here: https://www.continuum.io/downloads
  * It should be installed in your home, then change `$PATH` like this: https://stackoverflow.com/questions/18675907/how-to-run-conda
  * Create conda virtual environment, install package there: https://stackoverflow.com/questions/45707010/ipython-importerror-cannot-import-name-layout/45727917#45727917
  * To activate it, type `source activate conda_virtualenv`
  * To deactivate conda virtual environment, type `source deactivate`
  * To remove conda virtual environment, `conda remove -n yourenvname --all`, but note, to create conda virtual environment takes longer time than creating python `virtualenv`
    * After running the command line, you need to `cd anaconda/envs` and type `sudo rm -r yourenvname` to fully remove the environment
  * If you want to check how many conda virtual environment you have created and their names, also go to `anaconda/envs` by typing `cd anaconda/envs`


***************************************************************************************

<b>GitHub Commands</b>

* Clone to local folder: `sudo git clone https://github.com/hanhanwu/SFU_comments_extractor.git`
* Update local Git folder with the updates on GitHub: `git pull origin master`
* Choose GitHub license: https://choosealicense.com/
* How to create a license: https://help.github.com/articles/adding-a-license-to-a-repository/
* CC-BY-SA-4.0 for media data: https://choosealicense.com/licenses/cc-by-sa-4.0/#


***************************************************************************************

<b>WestGrid</b>

* Login: `ssh orcinus.westgrid.ca`
* Upload local fodler to WestGrid `scp -r [local path]/SFU_comments_extractor [my WestGrid id]@orcinus.westgrid.ca:[WestGrid path]`
* Run python3.5 through WestGrid Terminal:
  * `module load python/3.5.0`
  * `python3.5`
  
  
***************************************************************************************

<b>R Command</b>

* To find R HOME: `R.home()`, type this in R Studio
* Find my R packages in the previous version (this is why I hate version updating for some software...): `cd /Library/Frameworks/R.framework/Versions/3.2/Resources/library`

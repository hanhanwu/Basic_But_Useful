My RA work finally has been finished on 2017/4/29. So excited and I have collected all the comand lines used in MAC/Linux terminal, GitHub commnds, as well as WestGrid (cloud) commnds. 
This file will also be used to record other commands.

## Interact with Remote Linux Server

* Remote login to school Linux server: `ssh [my school id]@rcg-linux-ts1.rcg.sfu.ca` 
* Download folder from school server to local machine: `scp -r [my school id]@rcg-linux-ts1.rcg.sfu.ca:/rcg/sentiment/SOC/Factiva_Data/Factiva_Articles/2016 [local folder path]/RA`
* Send local folder to school server: `scp -r [local folder path]/2016_more [my school id]@rcg-linux-ts1.rcg.sfu.ca:/rcg/sentiment/SOC/Factiva_Data/Factiva_Articles`
* `scp` when there is space in your path: `scp [my school id]@rcg-linux-ts1.rcg.sfu.ca:"/rcg/sentiment/SOC/OnlineData/GlobeAndMail/all_online_data/all_online_data\ 2/empty_comment_ids.txt"  [local path]`
  * In a word, when there is space in your path, add `""` around the path and use `\ ` to replace the space 

## Mac Commnds

* <b>NOTE:</b> If it is showing any error, try to start your commnd line with `sudo`, if your know admin id and password.
* To simply open a folder/file: `open [folder_path/file_path]`
* Check folder memory: `du -sh`, use it under this folder
* Change root password: `sudo passwd root`
* To change `$PATH` temporarily, `export PATH="/some/new/path:$PATH"`
* Edit `~/.bash_profile`, if you are not good at editting a file through the command line (sometimes your command can totally overwrite the original file, which is not cool at all), why not just open the file and type in the text editor, save it. Do this `open ~/.bash_profile`, just like how you type in a text editor.
  * After saving the text file, you also need to run `source ~/.bash_profile` to make your edit valid.
* Install wget, `brew install wget`, wget is a commnd used to download things from an url
  * `wget url` to download
  * You can also use `curl -0 url` and it's built-in on Mac
* List in files in time order: `ls -lt`
* List files with created time: `ls -ll`
* Copy current folder to another folder: `cp -r f1 [new_dir path]/f1`
* Copy another folder to current folder `cp -r [folder_path] .`
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
  * `export PATH=/Library/Frameworks/Python.framework/Versions/3.5/bin:$PATH`
  * `export PATH=$PATH:/Users/devadmin/Documents/geckodriver`
* `brew update` error
  * When you try commands like `brew update`, it may show you error: `Error: The /usr/local directory is not writable.`
  * To deal with this, type `sudo chown -R $(whoami):admin /usr/local`, here no need to change anything in the command
  * After that, change permission back by typing `sudo chown root:wheel /usr/local`
* Python package Fully Uninstall
  * `sudo easy_install -m [PACKAGE]` or `sudo pip uninstall [package]`
  * `sudo rm -rf /usr/local/lib/python2.X/site-packages/[PACKAGE].egg` # remove egg file
* Find Python package: `pip show [package name]`, this will work even when you are using conda or python virtual environment.
* Having multiple types of Python
  * I have at least 3 types of python, all useful in different situations. Sometimes, I just want to switch to a certain type.
  * Switch between types temporarily:
    * `alias python="/usr/local/opt/python3/bin/python3.6"`
    * `alias python="/usr/local/opt/python3/bin/python2.7"`
    * Then when you type `python`, it will be the type you want
  * If your python2 is the default one, and `pip` only serves for python2. Even if you used `alias` switched to python3, pip still serves for the default python. The worst case will be, your pip3 no longer work any more (this could happen after Apple updated OS). Today I found a way works (I tried many other ways online, none of them worked....)
    * `/usr/local/opt/python3/bin/pip3 install [package]`
* Find a specific python package (such as networkx): `pip search networkx|grep networkx`
* After installing xcode, if you get this error `error: tool 'xcodebuild' requires Xcode, but active developer directory '/Library/Developer/CommandLineTools' is a command line `
  * Type `sudo xcode-select -s /Applications/Xcode.app/Contents/Developer`
  * Then type `sudo xcodebuild -license`, type `agree` at the end of that license
* Mac SDK
  * To check all the SDKs provided by Apple: `xcodebuild -showsdks`
  * To check SDK on your own machine: `xcrun --show-sdk-path`
* Install conda on Mac
  * First of all, download and install conda .pkg here: https://www.continuum.io/downloads
  * It should be installed in your home, then change `$PATH` like this: https://stackoverflow.com/questions/18675907/how-to-run-conda
    * Type `open ~/.bash_profile`
    * In the opened text file, copy `export PATH=~/anaconda/bin:$PATH`
    * Save the text file, and in the terminal type `source ~/.bash_profile`
  * Create conda virtual environment, install package there: https://stackoverflow.com/questions/45707010/ipython-importerror-cannot-import-name-layout/45727917#45727917
  * To activate it, type `source activate conda_virtualenv`
  * To deactivate conda virtual environment, type `source deactivate`
  * To remove conda virtual environment, `sudo conda remove -n yourenvname --all`, but note, to create conda virtual environment takes longer time than creating python `virtualenv`
    * After running the command line, you may need to `cd anaconda/envs` and type `sudo rm -r yourenvname` to fully remove the environment
  * If you want to check how many conda virtual environment you have created and their names, also go to `anaconda/envs` by typing `cd anaconda/envs`
* Check all the pyhton library versions: `pip freeze`
* Errors in intalling python packages
  * Error - "It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall."
    * `pip install --ignore-installed [PACKAGE-NAME]`
* About MacPorts, homebrew may give you an error, saying "You have MacPorts or Fink installed: /opt/local/bin/port"
  * So you can move the whole /local folder to a new folder called "macports", `sudo mv /opt/local ~/macports`
  * Oh, it seems that Homebrew and MacPorts do similar things, they download, compile, install and upgrade libraries... Is this the reason you will get an error in Homebrew?
* IPython find all kernels: Type `jupyter kernelspec list`
* Cannot open IPython for different reasons
  * Problem: "AttributeError: type object 'IOLoop' has no attribute 'initialized'"
    * `conda install -c conda-forge pyzmq`
    
## Windows Commands
### Python in Windows
* Download Anacoda to make you life easier: https://www.anaconda.com/download/
  * <b>Choose to add Anacoda in your PATH</b>, in this way you can use python through terminal directly
  * After installation, open your termonal: 
    * Type `python` and you can use python in the termnal
    * Or type `python --version` to check your python version
    * Or type `jupyter notebook` and you can use jupyter directly
### Windows Basic Commands
* List all files in current directory: `dir`

## GitHub Commands

* Clone to local folder: `sudo git clone https://github.com/hanhanwu/SFU_comments_extractor.git`
* Update local Git folder with the updates on GitHub: `git pull origin master`
* Choose GitHub license: https://choosealicense.com/
* How to create a license: https://help.github.com/articles/adding-a-license-to-a-repository/
* CC-BY-SA-4.0 for media data: https://choosealicense.com/licenses/cc-by-sa-4.0/#


## WestGrid

* Login: `ssh orcinus.westgrid.ca`
* Upload local fodler to WestGrid `scp -r [local path]/SFU_comments_extractor [my WestGrid id]@orcinus.westgrid.ca:[WestGrid path]`
* Run python3.5 through WestGrid Terminal:
  * `module load python/3.5.0`
  * `python3.5`
  
  
## R Command

* To find R HOME: `R.home()`, type this in R Studio
* Find my R packages in the previous version (this is why I hate version updating for some software...): `cd /Library/Frameworks/R.framework/Versions/3.2/Resources/library`

* Install packages such as "ChannelAttribution.tar.gz"
  * My goodness, I have never spent longer time to install an R package like this one
  * If you check online, they told you many different methods to install R package when you had failure
  * Now I think, a good starting point is to install from GitHub, if that package has a GitHub version, because the error messages in this install method is more detailed
    * `library(devtools)`
    * `install_github("cran/ChannelAttribution")`
    * Its GitHub: https://github.com/cran/ChannelAttribution
  * In this case, I got error telling me things maybe related to "clang", maybe related to "-lgfortran", I thought mayb ethat clang error caused by "-lgfortran", so I found the solution here:
    * Install -lgfortran: https://thecoatlessprofessor.com/programming/rcpp-rcpparmadillo-and-os-x-mavericks--lgfortran-and--lquadmath-error/
    * For mac Latest OS, download it here: http://gcc.gnu.org/wiki/GFortranBinaries#MacOS
    * Install the .dmg file
    * Then open you terminal, no matter which folder you are you, just type:
      * `mkdir ~/.R`, if you have already had this folder, the terminal you tell you that you had it. If you had it, type `cd ~/.R`, if `Makevars` is there, it's great.
      * Type `cat << EOF >> ~/.R/Makevars`
      * Type `FLIBS=-L/usr/local/gfortran/lib/gcc/x86_64-apple-darwin16/6.3.0 -L/usr/local/gfortran/lib -lgfortran -lquadmath -lm`, change the version name if you downloaded another version
      * Type `EOF`
    * Now in your RStudio, type `library(devtools)`, `install_github("cran/ChannelAttribution")`
  * You may still get the error after install&compile successfully. In this pack, it is important to check source code "LinkingTo"
    * Source: https://www.rdocumentation.org/packages/ChannelAttribution/versions/1.10
    * In LinkingTo, you will see `Rcpp`, `RcppArmadillo`. Install them all and restart your R session
  * Other note
    * Install from local file if you have downloaded the package
      * `install.packages("[zipped package local location]", repos = NULL, type="source")`
* `Error : .onLoad failed in loadNamespace() for 'rJava'....`
  * This error happened when I tried to install `subspace` package. The cause was because the link between Java_Home and R studio was not there or gor broken
  * First of all, check Java version by typing `java -version`
  * Next edit your bash profile
    * `open ~/.bash_profile`, this will open the bash_profile in the text editor for you
    * Copy `export JAVA_HOME="$(/usr/libexec/java_home -v 1.7)"` there and save it. The version here depends on your own Java version
    * To test,type `echo $JAVA_HOME`
  * They type `sudo ln -f -s $(/usr/libexec/java_home)/jre/lib/server/libjvm.dylib /usr/local/lib`, this will relink your java with R
  * `install.packages("rJava")`, then `library(rJava)`
  * `install.packages("subspace")`, then `library(subspace)`

## MySQL Commands

* Forgot Password & Reser Password - No matter whether you have MySQL workbench, when you are using your localhost, you need to start the server first. If you haven't used it for a while, you may realize, ahhhhh, I forgot the password
  * Step 1 - Open your terminal, make sure you have 2 folders under `/usr/local/`, "mysql" and "mysql-VERSION..."
  * Step 2 - Type `cd /usr/local/mysql`, then type `mysql.server start`
  * Step 3 - Open Mysql WORKBENCH, click "server status" on the left bar, it will ask you password to reset password. For old password, try to <b>leave it blank first</b>, since very possible, you didn't set the password before. Then set your new password
    * If you did set password before and forgot it, try the method here: https://www.howtoforge.com/setting-changing-resetting-mysql-root-passwords
  * Quit mysql in terminal, type `exit`
  * stop server, type `mysql.server stop`
  
* After MySQL didn't work...
  * I removed almost everything when I was cleaning the disk.... But I re-installed MySQL and made it work again
  * First of all, I removed folder `/usr/local/mysql`
  * `brew install mysql`, this will install MySQL under `/usr/local/mysql/var`
  * `brew services start mysql`
  * `mysql_secure_installation`, if you still remember your MYSQL root password, with this command, you can configure the settings
  * Now you can use MySQL Work Bench with connected server, or use MySQL in your terminal by typing `mysql -u root -p` & password for root
    * `exit` if you are using terminal and want to exit

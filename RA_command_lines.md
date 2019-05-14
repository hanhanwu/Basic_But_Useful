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
* When there is "dateutil" related errors
  * `sudo pip install python-dateutil --upgrade`, this one works
* Upgrade Python3
  * `brew install python3` (Optional if you already have python3 installed)
  * `brew update`
  * `brew upgrade python3`
  * Now try `python3 --version`, if it's still the older version:
    * try `brew link python`
    * If above doesn't work, try `brew link --overwrite python`
* Upgrade `xgboost` is a pain...
  * `sudo -H pip3 install -U setuptools`
  * Use `git clone` to install is better, https://xgboost.readthedocs.io/en/latest/build.html
    * You need to `cd xgboost`, then create "build" folder
    * Also in "xgboost" folder, type `cd python-package; sudo python setup.py install`
    * `export PYTHONPATH=~/xgboost/python-package`, tell pythonpath where to find the python package
  * If the installation succeeded, check xgboost version, `pip3 freeze | grep xgboost`
* Print python package version
  * `print(xgboost.__version__)`
* Python package Fully Uninstall
  * `sudo easy_install -m [PACKAGE]` or `sudo pip uninstall [package]`
  * `sudo rm -rf /usr/local/lib/python2.X/site-packages/[PACKAGE].egg` # remove egg file
* Find Python package: `pip show [package name]`, this will work even when you are using conda or python virtual environment.
* Having multiple types of Python
  * I have at least 3 types of python, all useful in different situations. Sometimes, I just want to switch to a certain type.
  * Switch between types temporarily:
    * `alias python="/usr/local/opt/python3/bin/python3.6"`
    * `alias python=python3`
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
* Check specific python package version: `pip freeze | grep scikit-learn`
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
* <b>Install AWS CLI (command line tool)</b>
  * Just type `sudo -H pip install awscli --upgrade --ignore-installed six` worked for me
  * The guidance in AWS website didn't really work for me: https://docs.aws.amazon.com/cli/latest/userguide/install-macos.html#awscli-install-osx-path
  * Type `aws --version` to see whether you got it installed
  * When creating `~/.aws/credentials` or `~/.aws/config`, you will need accedd id and secret access key, to find them, check this: https://help.bittitan.com/hc/en-us/articles/115008255268-How-do-I-find-my-AWS-Access-Key-and-Secret-Access-Key-
    * You may need to click "Create Access key" in order to see your secret access key

## AWS EC2 Troubleshooting
* I chose a task to learn AWS skills, who knows even basic setup can be troublesome. Let me take a note.
### Jupyter Lab
* Could not import `pandas` even the installation is all succeeded in both python3 and python2.
  * In the terminal, type `sudo apt-get remove ipython`, then `sudo apt autoremove`. At least you can still use `sudo`, so it's lucky.
### `aws` Command line
* Without setting the profile, it will use EC2 instance profile, which has "None" for all the access id, secret access key
  * To set profile for AWS, check https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html, "Quick Configuration and Multiple Profiles"
  * This can be confusing, since when you are creating an EC2 instance through AWS CLI, the profile has already been set with specific access key and access id, howcome the default one has all values as None...
    
## Windows Commands
### Python in Windows
* Download Anacoda to make you life easier: https://www.anaconda.com/download/
  * <b>Choose to add Anacoda in your PATH</b>, in this way you can use python through terminal directly
  * After installation, open your termonal: 
    * Type `python` and you can use python in the termnal
    * Or type `python --version` to check your python version
    * Or type `jupyter notebook` and you can use jupyter directly
  * After installing Anaconda, later when you are using `pip` to install any libraries, they will be saved in `Anaconda/lib/site-packages/` automatically
* Download and install `pip`
  * Download pip: `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`, oh windows can use curl...
  * Install pip: `python get-pip.py`
* Install Tensorflow
  * Install: `pip install --upgrade tensorflow`
  * Verify version: `python -c "import tensorflow as tf; print(tf.__version__)"`
* Install Keras
  * `pip install keras`
  * If it will show your keras is not compatable with tensorflow, open `Anaconda/Lib/site-packages/tensorflow/tools/pip_package/setup.py` and change these 2 lines to your keras version:
    * `keras_applications >= 1.0.5`,
    * `keras_preprocessing >= 1.0.3`
* Install XGBoost
  * `anaconda search -t conda xgboost`, this one is just to show what you can install through conda on difference OS and python verison
  * `conda install -c anaconda py-xgboost`, you can choose this one or other versions
* Load Spacy "en" model
  * Run your terminal as admin, tyen type in the terminal `python -m spacy download en`
* Install Pytorch
  * `conda install pytorch torchvision cuda91 -c pytorch`
### Windows Basic Commands
* List all files in current directory: `dir`
* Print out current path on windows: `cd`
* Show hidden files on current location: `dir /ah`
* How to use `git` in windows terminal
  * Just download it and install: https://gitforwindows.org/
  * You don't have to config your username/email, just type `git clone [URL]`, and you can download the package.
* How to open Disk Management
  * My Win search doesn't work on this.
  * Press `Win` then type `run`
  * In the open blank box, type `diskmgmt.msc`
### Other intall on Windows
* How to install Visual C++ 14.0: https://www.scivision.co/python-windows-visual-c++-14-required/
* How to install `fastai`
  * I haven't had my breakfast but decided to write these down here, is because the installation of fastai really gave me a hard time last night, on both mac and windows. Finally I had to leave it install during the night, Saturday is supposed to be the time when I can get much more sleep. Fastai installation, totally broke my plan.
  * Install above Visual C++ 14 on wwindows
  * <b>Strongly recommend to have anaconda ready, some packages used here will have problems when installing with pip.</b>
  * The latest fastai 1.0 has problems, better to install fastal 0.7. 
    * If you installed fastai with pip or anaconda without setting version, uninstall it first, `pip uninstall fastai`
    * `pip install Pillow==4.1.1`
    * `pip install "fastai==0.7.0"`
    * If during any installation, you will seeing version incompatible warnings, upgrade those libraries. For example, update `pandas` by using `pip install --upgrade pandas`
    * `pip install -U opencv-python`
    * `pip install image`
    * Install pytorch, which created most of the pain. After each "try" below, check whenther you can run `from fastai.imports import *` in python.
      * Try its official installation method, `conda install numpy pyyaml mkl mkl-include setuptools cmake cffi typing`, this may gave you many errors
      * Then try `conda update conda`
      * Try `conda install mkl=2018`
      * Try `conda install pytorch torchvision -c pytorch`, this may also gave errors, but try it
      * Try `conda install -c peterjc123 pytorch cuda90`
  * If you don't want to see warnings, run these in python:
    * `import warnings`
    * `warnings.filterwarnings("ignore", category=DeprecationWarning)`
* How to install `fbprophet`
  * `conda install libpython m2w64-toolchain -c msys2`
  * `conda install numpy cython -c conda-forge`
  * `conda install matplotlib scipy pandas -c conda-forge`
  * `pip install pystan`
  * `conda install -c conda-forge fbprophet`
* "WinError: dot cannot be found", how toinstall `graphviz`
  * pip install on windows won't work... You need to download the .zip file here first: https://graphviz.gitlab.io/_pages/Download/Download_windows.html
    * Then put the path of the "bin" file into environmental variable
  * `pip install pydot` won't work, even it's successfully installed. Only conda install is supported on windows... Type `conda install -c anaconda graphviz`
    
### Install Linux on Removable Hard Drive
* All these months, failed too many times. Finally, it got installed successfully during this long weekend. I'm feeling so happy.
* I just want to install the OS on my 5TB removable hard drive. But it is NSFT format and can only be used on Windows. So my first 1/3 time was used on my mac... anyway it's a learning experience. Finally, decided to install on my windows.
* The detailed process can be found here: https://askubuntu.com/questions/1081839/how-to-make-virtualbox-use-removable-hard-drive-memory-automatically/1081847#1081847
  * VirtualBox was installed in my local machine. Mormally it will be installed under `C:\Program Files\Oracle\VirtualBox`.
  * Then in my terminal I set the path for `VBoxManage` by typing `set PATH=%PATH%;"C:\Program Files\Oracle\VirtualBox"`
    * So that I can use `VBoxManage createhd --filename "D:\Hanhan_VirtualBox\Hanhan_Linux64\Hanhan_Linux64.vdi" --size 1048576 --format VDI --variant Fixed` to set virtual hard drive using my removable hard drive space. 
  * I had to download ubuntu .iso from ubuntu website even though in the virtual box I have already chosen the Unbuntu.
  * After starting the virtual machine, it asked to install Ubuntu, but in fact that environment is already the Unbuntu. You can type `lsb_release -a` in Ubuntu terminal to check the version.
  
## Linux Commands
* Install `curl`: `sudo apt install curl`
  * You may get error saying "cannot get lock /var/lib/apt/lists/lock...", type `sudo rm /var/lib/apt/lists/lock` to solve the problem.
* Install whois
  * whois searches for an object in a WHOIS database. WHOIS is a query and response protocol that is widely used for querying databases that store the registered users of an Internet resource, such as a domain name or an IP address block, but is also used for a wider range of other information.
  * `sudo apt-get update`
  * `sudo apt-get install whois`
* To exit nslookup
  * `exit`
  * nslookup is built in many systems

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

My RA work finally has been finished on 2017/4/29. So excited and I have collected all the comand lines used in MAC/Linux terminal, GitHub commnds, as well as WestGrid (cloud) commnds. 
This file will also be used to record other commands.

## Interact with Remote Linux Server
* Remote login to school Linux server: `ssh [my school id]@rcg-linux-ts1.rcg.sfu.ca` 
* Download folder from school server to local machine: `scp -r [my school id]@rcg-linux-ts1.rcg.sfu.ca:/rcg/sentiment/SOC/Factiva_Data/Factiva_Articles/2016 [local folder path]/RA`
* Send local folder to school server: `scp -r [local folder path]/2016_more [my school id]@rcg-linux-ts1.rcg.sfu.ca:/rcg/sentiment/SOC/Factiva_Data/Factiva_Articles`
* `scp` when there is space in your path: `scp [my school id]@rcg-linux-ts1.rcg.sfu.ca:"/rcg/sentiment/SOC/OnlineData/GlobeAndMail/all_online_data/all_online_data\ 2/empty_comment_ids.txt"  [local path]`
  * In a word, when there is space in your path, add `""` around the path and use `\ ` to replace the space 

## SQL Server Commands

* `sp_spaceused "[table_name]"` will get you the table size even if you don't have the permission to access info schema table
  
## Git Commands
* If you have multiple github accounts, and want to make sure you are using the right account to commit and push:
  * Method 1 - Change git config username and email:
    * To check what's your current username and email, type `git config --list`
    * Type `open ~/.gitconfig` in your terminal, and you should be able to change the username as well as the email
  * Method 2 - Specify the "author" in pychram git commit
    * When you start to commit, on Pycharm UI, there is "author" and you can choose the right one to commit 
* Connect to Github with ssh: https://docs.github.com/en/enterprise/2.18/user/github/authenticating-to-github/connecting-to-github-with-ssh
* `git branch -v` to check current branch of the repository
* `git remote -v` to check where does local repository point to
* Update changes from the cloned directory: 
  * `cd` to that folder locally first
  * `git remote add upstream https://github.com/hanhanwu/mlflow-example.git`
  * `git pull upstream master`
    * `master` is the branch name
* [How to add an existing project into Github][2]
* Clone to local folder: `sudo git clone https://github.com/hanhanwu/SFU_comments_extractor.git`
* Update local Git folder with the updates on GitHub: `git pull origin master`
  * `master` is the branch name
* Choose GitHub license: https://choosealicense.com/
* How to create a license: https://help.github.com/articles/adding-a-license-to-a-repository/
* CC-BY-SA-4.0 for media data: https://choosealicense.com/licenses/cc-by-sa-4.0/#

## Docker Commands
* Docker concepts and basic commands: https://www.analyticsvidhya.com/blog/2021/10/a-complete-guide-on-docker-for-beginners/?utm_source=feedburner&utm_medium=email&utm_campaign=Feed%3A+AnalyticsVidhya+%28Analytics+Vidhya%29
* `docker images` to list all the images and their tags as well as other attributes
* `docker-compose run shell` to start the docker container
  * Sometimes your docker env may not be built well, even after entering this env, code may not be runable, to fix this issue, you can try to re-build the container:
    * `docker system prune` to remove all the docker containers
    * `docker-compose build` to rebuild the container 
* Docker Playground: https://www.docker.com/101-tutorial
  * To try docker commands without any setup
  * Start with running `docker run -dp 80:80 docker/getting-started:pwd`

## Linux Commands (different from Mac)
* How to install Homebrew
  * `git clone https://github.com/Homebrew/brew ~/.linuxbrew/Homebrew`
  * `mkdir ~/.linuxbrew/bin`
  * `ln -s ~/.linuxbrew/Homebrew/bin/brew ~/.linuxbrew/bin`
  * `eval $(~/.linuxbrew/bin/brew shellenv)`

## Language R on Jupyter
* The interface of R Notebook on R studio is too painful to use and the saved file cannot be shown on github well. Just found, we can use R on jupyter notebook. [How to install R kernel on jupyter][4]
  * If it's your first time to install anaconda, you can included R kernel from there
* To install R packages through jupyter, open "Console" with R kernel, then type `install.packages('[package_name]')` 

## Airflow
* How to install locally: https://airflow.apache.org/docs/apache-airflow/stable/start/local.html
  * Better to use Mac or Linux, if want to install on Window, you will get error saying module `termios` can't be found, in fact this library is not available on windows...
* Each time to start airflow, just type `airflow standalone` in the terminal
  * Open http://localhost:8080/home to run pipelines 
* To add your own .py as a new DAG to localhost:
  * Make sure you have run `export AIRFLOW_HOME=~/airflow`
  * Open you airflow folder, find file `airflow.cfg` and open it, make sure the dags folder looks like this `dags_folder = ~/airflow/dags`
  * Then you can add your DAG .py file under `~/airflow/dags`
    * In your .py file, make sure to define the `dag_id`, that will be the file name shown in the dag list of your localhost
    * You can also type command `airflow dags list` under folder `~/airflow`, it will list all the dags you would see in the localhost
* To use any python package, make sure it has been install in the site packages of the python used by your airflow
* How to set `schedule_interval` for the DAG: https://crontab.guru/

## Mac Commands
* How to install SQL Workbench on Mac: https://data36.com/install-sql-workbench-postgresql/
  * Build 124 will work: https://www.sql-workbench.eu/download-archive.html
* How to run `.sh` file through terminal, assume the file name is "run.sh"
  * `chmod +x run.sh` sets execution permission
  * `./run.sh` runs the script
* Change Mac shells
  * List available shells: `cat /etc/shells`
  * I often use sh, so `chsh -s /bin/sh`
  * You can also use mac UI: https://apple.stackexchange.com/questions/88278/change-default-shell-from-bash-to-zsh
* <b>NOTE:</b> If it is showing any error, try to start your commnd line with `sudo`, if your know admin id and password.
* To simply open a folder/file: `open [folder_path/file_path]`
* Check folder memory: `du -sh`, use it under this folder
* Change root password: `sudo passwd root`
* To change `$PATH` temporarily, `export PATH="/some/new/path:$PATH"`
* `which python3` to get the path of current python3, also check `brew info python3`, since `which python3` may not tell you the location installed by brew
* Edit `~/.bash_profile`, if you are not good at editting a file through the command line (sometimes your command can totally overwrite the original file, which is not cool at all), why not just open the file and type in the text editor, save it. Do this `open ~/.bash_profile`, just like how you type in a text editor.
  * After saving the text file, you also need to run `source ~/.bash_profile` to make your edit valid.
* Install wget, `brew install wget`, wget is a commnd used to download things from an url
  * `wget url` to download
  * You can also use `curl -0 url` and it's built-in on Mac
* Install mysqlclient
  * Install MySQL server through brew: https://tableplus.com/blog/2018/11/how-to-download-mysql-mac.html
  * Install `openssl`
  * Run this command
    * Latest mysqlclient: `LDFLAGS=-L/usr/local/opt/openssl/lib pip install mysqlclient`
    * Specific version: `LDFLAGS=-L/usr/local/opt/openssl/lib pip install mysqlclient==1.4.6`
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
  * `nohup`
    * Using `nohup` for python file: `sudo nohup python3.5 SFU_comments_extractor/source/ScrapeNews/get_comment_reactions.py`
    * Using `nohup` for .sh file: `sudo nohup sh run_news_scraper.sh`
    * `nohup` creates a log in the folder where you are running the `nohup` job, easier for debugging if necessary
  * `screen`
    * Using `screen`: `sudo screen python3.5 SFU_comments_extractor/source/ScrapeNews/get_comment_reactions.py`
    * Using `screen` for EC2 process
      * ssh into your EC2 remote box, type `screen`
      * Then run the process you want
      * `Ctrl + A` then `Ctrl + D` to detatch the screen session
        * EC2 box might logout automatically, and will kill your running process. So <b>better to do this step right after running the process</b> (if your process works fine). Otherwise the screen cannot be resumed after EC2 box logged out.
      * `screen -r` to resume the screen session
        * If your process is finished, there is no session to resume
  
* When it's showing "no space left on the device" during packages installation
  * The reason caused the problem might be because of the small partition in your virtual env
    * Try `pip install -r requirements.txt --build=~/tmp/build/`, it's `--build=~/tmp/build/` makes a difference
    * If it doesn't work, try upgrade pip first, `/usr/bin/python3 -m pip install --upgrade pip`
  * You can check filesystem availability through `df -h`
* Add a library path to `$PATH`
  * `export PATH=/Library/Frameworks/Python.framework/Versions/3.5/bin:$PATH`
  * `export PATH=$PATH:/Users/devadmin/Documents/geckodriver`
* Add permission to run a python package, such as Ray
  * ` sudo chmod -R a+wxr /home/venv/lib/python3.6/site-packages/ray` to enable the permission of the certain package
* `brew update` error
  * When you try commands like `brew update`, it may show you error: `Error: The /usr/local directory is not writable.`
  * To deal with this, type `sudo chown -R $(whoami):admin /usr/local`, here no need to change anything in the command
  * After that, change permission back by typing `sudo chown root:wheel /usr/local`
* When there is "dateutil" related errors
  * `sudo pip install python-dateutil --upgrade`, this one works
* Upgrade Python3 through Python Homepage
  * If your python installed under `/Library/Frameworks/Python.framework/Versions`, that means they came from Python homepage, brew install cannot really overwrite current version (even you tried all types of brew link)
  * Just download the latest version from Python homepage here: https://www.python.org/downloads/
* Install homebrew on mac
  * `sudo chown -R $(whoami) $(brew --prefix)/*` grant the permission first
  * Install brew: https://brew.sh/
* Brew install packages
  * You company might block brew from downloading those packeages
    * Download the package manually (the url should be shown in the terminal), such as "https://yarnpkg.com/downloads/1.22.10/yarn-v1.22.10.tar.gz"
    * After successfuly downloading, run `mv Downloads/yarn-v1.22.10.tar.gz $(brew --cache -s yarn)`
    * Restart the brew install
* How to install multiple python versions
  * `brew unlink python` if you want to switch the existing python version to another one 
  *  `brew install python@3.7`
  * `brew list | grep python`
  * `brew ls python@3.7`
  * `ls -l /usr/local/Cellar/python@3.7/3.7.8_1/bin/python3.7`
  * `ln -s /usr/local/Cellar/python@3.7/3.7.8_1/bin/python3.7 /usr/local/bin/python3.7`
  * `python3.7 -V`
  * `python3.7 -m venv venv37`
  * `source venv37/bin/activate`
  * `deactivate`
  * When using Pycharm to find a specific version to create the virtual env, the locaion is like "~/venv37/bin/python3.7"

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
* Having multiple types of Python/Install python on mac
  * I have at least 3 types of python, all useful in different situations. Sometimes, I just want to switch to a certain type.
  * Change Default Python Permanently
    * Find python location
      * Default location by checking `which python` or `which python3`
      * If python is downloaded through https://www.python.org/downloads/, location might be "/Library/Frameworks/Python.framework/Versions/3.9", or at least check "/Library/Frameworks/" to find the right python version you want
    * Find python site packages
      * Run python through terminal, then type `import site; site.getsitepackages()` should output the path
    * `open ~/.bash_profile`, open the file
    * Add `alias python='python3'` and savethe file
    * `source ~/.bash_profile`
    * `python --version` to check default python version now
  * How to install pip without using brew: https://pip.pypa.io/en/stable/installing/
    * For python3 run `python3 get-pip.py`
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
      * It seems that after anaconda 2019.10, it will edit ~/.bash_profile for you while the installation
    * Save the text file, and in the terminal type `source ~/.bash_profile`
  * Create conda virtual environment with specified version: https://stackoverflow.com/questions/45707010/ipython-importerror-cannot-import-name-layout/45727917#45727917
  * Create a conda env, type `conda create --name venv`
    * List all the conda virtual environments: `conda env list`
  * To activate it, type `conda activate conda_venv`
  * Now to check whether there is ipython, you can just type `jupyter lab` or `jupyter notebook` and it will work
    * To add the virtual env into ipython kernel:
      * `pip install ipykernel`
      * `python -m ipykernel install --user --name conda_virtualenv --display-name "Python3 (venv)"`
        * Change the values for `--name` and `--display-name`   
  * To deactivate conda virtual environment, type `conda deactivate`
  * To remove conda virtual environment, `sudo conda remove -n venv --all`, but note, to create conda virtual environment takes longer time than creating python `virtualenv`
    * After running the command line, you may need to `cd anaconda/envs` and type `sudo rm -r venv` to fully remove the environment
  * IPython find all kernels (environments): Type `jupyter kernelspec list`
  * To remove a certain environment, `jupyter kernelspec uninstall [myenv]`
* Uninstall anaconda on Mac
  * Normally Anaconda has a folder under your Username, so just do `sudo rm -r anaconda`
  * `echo $PATH` and check whether anaconda is in the $PATH, if so, `open ~/.bash_profile` and remove/comment the anaconda path
* When it's not conda virtual environment
  * `pip install virtualenv`
  * Create virtual environment `virutalenv -p python3 venv`
    * Sometimes this won't work if you have many python versions on your machine, like I do..., try `python3 -m virtualenv venv`
  * Activate virtual env `source venv/bin/activate`
* Check all the pyhton library versions: `pip freeze` or `pip list`
* Check specific python package version: `pip freeze | grep scikit-learn`
* Save pip freeze in file: `pip freeze -l > requirements.txt`, this also works in virtual env, and make sure you are running this command under the right virtual env
* Errors in intalling python packages
  * Error - "It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall."
    * `pip install --ignore-installed [PACKAGE-NAME]`
* About MacPorts, homebrew may give you an error, saying "You have MacPorts or Fink installed: /opt/local/bin/port"
  * So you can move the whole /local folder to a new folder called "macports", `sudo mv /opt/local ~/macports`
  * Oh, it seems that Homebrew and MacPorts do similar things, they download, compile, install and upgrade libraries... Is this the reason you will get an error in Homebrew?
* Cannot open IPython for different reasons
  * Problem: "AttributeError: type object 'IOLoop' has no attribute 'initialized'"
    * `conda install -c conda-forge pyzmq`

## AWS Cli
* `aws --version` to check installed version
* `aws s3 ls` to list S3 buckets you can see

#### Install AWS CLi v1
* Just type `sudo -H pip install awscli --upgrade --ignore-installed six` worked for me
* The guidance in AWS website didn't really work for me: https://docs.aws.amazon.com/cli/latest/userguide/install-macos.html#awscli-install-osx-path
* Type `aws --version` to see whether you got it installed
* When creating `~/.aws/credentials` or `~/.aws/config`, you will need accedd id and secret access key, to find them, check this: https://help.bittitan.com/hc/en-us/articles/115008255268-How-do-I-find-my-AWS-Access-Key-and-Secret-Access-Key-
  * You may need to click "Create Access key" in order to see your secret access key
#### Install AWS Cli v2
* Download and intsall: https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-mac.html
* In your terminal, type `aws configure`
  * It will ask for your access key id and secret key, see how to create them: https://aws.amazon.com/blogs/security/wheres-my-secret-access-key/
  * This command will also generate "~/.aws/credentials" and "~/.aws/config" files automatically 
#### Check S3 Access
* `cd ~/.aws` get to AWS folder
* `aws s3 ls`, if you have the right access, you should be able to see the listed folders under your S3 default credentials

## AWS EC2
### Create SSH keys
* Don't use the same one used by Github
* Use the commands here: https://docs.joyent.com/public-cloud/getting-started/ssh-keys/generating-an-ssh-key-manually/manually-generating-your-ssh-key-in-mac-os-x
### Jupyter Lab / Jupyter Notebook
* Could not import `pandas` even the installation is all succeeded in both python3 and python2.
  * In the terminal, type `sudo apt-get remove ipython`, then `sudo apt autoremove`. At least you can still use `sudo`, so it's lucky.
* `%whos` - Show the list of variables
* `%history` - Show all commands
  * `%history -o` - Print commands as well as output
  * `%history -n -t` - Print commands that has been translated into valid python commands
* `%prun` - Majorly about time efficiency of the code
### `aws` Command line
* Without setting the profile, it will use EC2 instance profile, which has "None" for all the access id, secret access key
  * To set profile for AWS, check https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html, "Quick Configuration and Multiple Profiles"
  * This can be confusing, since when you are creating an EC2 instance through AWS CLI, the profile has already been set with specific access key and access id, howcome the default one has all values as None...
* How to install Homebrew
  * `git clone https://github.com/Homebrew/brew ~/.linuxbrew/Homebrew`
  * `mkdir ~/.linuxbrew/bin`
  * `ln -s ~/.linuxbrew/Homebrew/bin/brew ~/.linuxbrew/bin`
  * `eval $(~/.linuxbrew/bin/brew shellenv)`
* How to install mysqlclient
  * https://pypi.org/project/mysqlclient/
### Check GPU Performance
* `pip install gpustat`
 * Later just run `gpustat -i 5 -cp`
* `htop`
### Save the screen
* `screen -S session_name`, define the session_name yourself
### Netcat
* It's available on mac but you need to download and install on windows. However, when I was downloading netcat from official nmap page, my security system detected trojan virus, which is normal for these files.
* `nc -lk [port number]` to start TCP connection
* `python3 my_file.py localhost [port number]` to run the python streaming code
* Ctrl + C to end the connection
### [How to install spark on Mac][1]
* In 2021 I found to export java_home in this way works: https://stackoverflow.com/questions/6588390/where-is-java-home-on-macos-mojave-10-14-to-lion-10-7
### DBFS Cli, Databricks Cli
* How to find HOST URL: https://docs.databricks.com/workspace/workspace-details.html#workspace-url
* `pip install databricks-cli`, `pip install databricks-cli --upgrade` to install or upgrade databricks cli
* `dbfs configure --token`
  * Type HOST
  * Type Token
    * How to create/find the token: https://docs.databricks.com/dev-tools/api/latest/authentication.html
* DBFS commands
  * `dbfs ls`
  * `dbfs cp [local file path] [DBFS file path] --overwrite` 
    * `dbfs` or `databricks fs` has to be there and before `cp`
* How to get access to Azure storage: https://docs.microsoft.com/en-us/azure/databricks/data/data-sources/azure/azure-storage#access-azure-blob-storage-using-the-dataframe-api
  * Only config in databricks cluster may not be enough, in databricks notebook, still need to use `spark.conf.set()` 

### Databricks Settings
* Databricks has a new function - autoscaling pool. When your cluster is pointing to the pool, the more users on it the more likely your notebook will encounter a scaled-up cluster (and the faster your stuff will run from a cold start)
  * The setup is just to point the worker and driver to the created pool
  * https://docs.microsoft.com/en-us/azure/databricks/clusters/instance-pools/cluster-instance-pool 
* When you get error showing hive metastore version mismatch when running a sql query in Databricks, add these in spark config:
  * `spark.sql.hive.metastore.jars builtin`
  * `spark.sql.hive.metastore.version 1.2.1`  # change the version here as what you need
  * `spark.databricks.delta.preview.enabled true` 
* How to link databricks to databricks: 
  * This allows you to save notebooks as `.ipynb` format but may not link to github well: https://docs.microsoft.com/en-us/azure/databricks/notebooks/github-version-control
  * This is allows you to update changes with github and pull, and can guarantee to link to github correctly: https://docs.microsoft.com/en-us/azure/databricks/repos
    * But notebooks will be saved as `.py` format

    
## Windows Commands
### [Suggestions to prevent battery draining][3]
  * I really don't think Windows is designed for lazy people... It has so many automatic problems waiting for you to resolve.
  * Better not to disable the index
  * Check whether there is power errors
    * Open terminal as admin
    * `powercfg/energy`
    * Open the .html file in your browser
  * If it's showing high processor usage as the error, check system updates, updating the system and restart the machine
  
### Python in Windows
* Check all the python versions installed: `py -0p`
* Download Anacoda to make you life easier: https://www.anaconda.com/download/
  * <b>Choose to add Anacoda in your PATH</b>, in this way you can use python through terminal directly
    * If didn't choose that option, check this to add conda and python into `Path`: https://www.datacamp.com/community/tutorials/installing-anaconda-windows
      * conda can be added in user variable `Path`
      * python needs to be added in system variable `Path`
      * But better to choose that option, otherwise jupyter notebook cannnot be opened...
  * After installation, open your terminal: 
    * Type `python` and you can use python in the termnal
    * Or type `python --version` to check your python version
    * Or type `jupyter notebook` and you can use jupyter directly
  * After installing Anaconda, later when you are using `pip` to install any libraries, they will be saved in `Anaconda/lib/site-packages/` automatically
  * Check all the virtual env you have created: `conda env list`
  * To activate a env: `conda activate [env_name]`
  * All the conda virtual env commands: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html
* Download and install `pip`
  * Download pip: `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`, oh windows can use curl...
  * Install pip: `python get-pip.py`
* Install PyTorch GPU
  * Follow this video: https://www.youtube.com/watch?v=GMSjDTU8Zlc
  * You might need to delete `caffe2_observers.dll`, `caffe2_module_test_dynamic.dll`, `caffe2_detectron_ops.dll` if getting error of loading these files when running `import torch`
  * Verification commands to ensure PyTorch GPU is enabled:
    * `import torch`
    * `print(torch.cuda.is_available())` should get `True`
    * `print(torch.cuda.get_device_name(0))` should return your GPU name
  * You can go to "Task Manager" --> "Performance" to check the GPU usage on Windows
* How to enable for tensorflow GPU
  * <b>Strongly recommend to use a virtual env for the setup</b>
  * This is the best tutorial I found: https://www.youtube.com/watch?v=qrkEYf-YDyI
  * Make sure software versions exactly align with Tensorflow's requirements: https://www.tensorflow.org/install/gpu#software_requirements 
  * If you will get error when checking whether GPU is available in the last step, might need to rename file name:https://stackoverflow.com/questions/65608713/tensorflow-gpu-could-not-load-dynamic-library-cusolver64-10-dll-dlerror-cuso
  * Sometimes you may get error saying there is no memory to allocate, then you might need to reduce batch_size and input data size, but this may also make GPU version slower than CPU version
    * To switch between CPU and GPU, write your model training code under `with tf.device("/cpu:0"):` (use CPU) or `with tf.device("/gpu:0"):` (use GPU)
  * Older experiments: https://github.com/hanhanwu/Hanhan_Data_Science_Practice/blob/master/AI_Experiments/after_2020/use_local_windows_GPU.md
* Install Tensorflow
  * Download and install the latets Visual C++: https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads
  * Install: `pip install --upgrade tensorflow --user`
  * Verify version: `python -c "import tensorflow as tf; print(tf.__version__)"`
  * Install tensorflow addons (tfa): `pip install tensorflow-addons[tensorflow]`, when import it, type `import tensorflow_addons`
* Install Keras
  * `pip install keras`
  * If it will show your keras is not compatable with tensorflow, open `Anaconda/Lib/site-packages/tensorflow/tools/pip_package/setup.py` and change these 2 lines to your keras version:
    * `keras_applications >= 1.0.5`,
    * `keras_preprocessing >= 1.0.3`
* Install XGBoost
  * `anaconda search -t conda xgboost`, this one is just to show what you can install through conda on different OS and python verison
  * `conda install -c anaconda py-xgboost`, you can choose this one or other versions
* Load Spacy "en" model
  * <b>Run your terminal as admin</b>, type type in the terminal `python -m spacy download en`
    * Make sure you have already installed spacy by running `pip install spacy`
    * The reason to run as admin is to create a shortcut link for "en"
* Install Pytorch
  * `conda install pytorch torchvision cuda91 -c pytorch`
* Install facebook prophet
  * Download and install the latets Visual C++: https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads
  * Run the terminal as admin, and activate the virtual environment
  * `conda install libpython m2w64-toolchain -c msys2`
  * `pip install fbprophet`
* Install PyMC3
  * Run these commands: https://anaconda.org/conda-forge/pymc3
  * Install Theano through: `pip intsall Theano`
### Windows Basic Commands
* List all files in current directory: `dir`
* Print out current path on windows: `cd` or `chdir`
* Show hidden files on current location: `dir /ah`
* Remove a folder
  * `rmdir my_folder` is to remove an empty folder
  * `rmdir /s my_folder` is to remove an unempty folder
* How to use `git` in windows terminal
  * Just download it and install: https://gitforwindows.org/
  * You don't have to config your username/email, just type `git clone [URL]`, and you can download the package.
* How to open Disk Management
  * My Win search doesn't work on this.
  * Press `Win` then type `run`
  * In the open blank box, type `diskmgmt.msc`
* When powershell script got disabled
  * `Set-ExecutionPolicy RemoteSigned` will only download scripts must be signed by a trusted publisher.
    * See other options: https://tecadmin.net/powershell-running-scripts-is-disabled-system/
* Open current folder as a prompt window
  * `start.`

### Other intall on Windows
* Install Git
  * https://git-scm.com/download/win
* How to install Visual C++ 14.0: https://www.scivision.co/python-windows-visual-c++-14-required/
* How to install `fastai`
  * I haven't had my breakfast but decided to write these down here, is because the installation of fastai really gave me a hard time last night, on both mac and windows. Finally I had to leave it install during the night, Saturday is supposed to be the time when I can get much more sleep. Fastai installation, totally broke my plan.
  * Install above Visual C++ 14 on windows
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
* To install `graphviz` on Mac
  * Either you can try anaconda
  * Or:
    * `ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" < /dev/null 2> /dev/null ; brew install caskroom/cask/brew-cask 2> /dev/null`
    * `brew install graphviz`
      * You may get some instructions at the end to tell you add those libraries into PATH, in fact, ignore them is also fine
* How to install `ray`
  * Check this page first: https://docs.ray.io/en/master/installation.html
  * It just started to support windows from 2020, and the "stable version" may create error. Better to install the latest snapshots: https://docs.ray.io/en/master/installation.html#latest-snapshots-nightlies
  * `pip install ray[dashboard]`
  * Make ray dashboard works
    * Install `npm` https://phoenixnap.com/kb/install-node-js-npm-on-windows
      * After the installation, put "C:\Program Files\nodejs" in "User Variable" of system variables
      * If you installed additional libraries, including the python newest version you don't want, go to windows "uninstall programs", find that python version and uninstall it, otherwise your python default version might be replaced.
    * Go to site-packages to find ray\dashboard, mine is `anaconda3\Lib\site-packages\ray\dashboard\`
      * If you cannot find `client` folder, download the whole project from https://github.com/ray-project/ray
      * Copy those files, folders you are missing in your local `dashboard\` folder
      * `cd client`
      * `npm ci`
      * `npm build`
  * Also make sure there is no other folder called "ray" under the same fodler where you are importing ray.
* How to install `tsfresh` (Optional)
  * Have to use conda, `conda install -c conda-forge tsfresh`, it might failed in the first 2 attempts 

### Windows Subsystem Linux (WSL)
* Download and install Ubuntu:
  * Note: I tried to use windows store to download Ubuntu, but unfortunately it could not be installed. Windows really sucks, and it took so much time to wait for windows store to load...
  * Download Ubuntu through Powershell: `Invoke-WebRequest -Uri https://aka.ms/wsl-ubuntu-1804 -OutFile Ubuntu.appx -UseBasicParsing`
  * Install the distro: `Add-AppxPackage .\Ubuntu.appx`
* Launch the installed Unbuntu
  * Just click the windows sign, and launch it. It's fast and smooth
  * `sudo apt update && sudo apt upgrade` to upgrade to the latest distro
* How to install & launch the User Interface for WSL
  * Download and install windows X server on windows: https://sourceforge.net/projects/vcxsrv/
  * Launch X server through `C:\Program Files\VcXsrv\xlaunch`
  * In your linux terminal, type:
    * `sudo apt install lxde`
    * `export DISPLAY=:0`
    * `export LIBGL_ALWAYS_INDIRECT=1`
    * `startlxde`
### Install Kafka on Windows
#### Option 1 - Install on WSL (Windows Subsystem Linux)
* Install WSL
  * Follow the steps here: https://docs.microsoft.com/en-us/windows/wsl/install-win10#step-4---download-the-linux-kernel-update-package
  * If step 4 gives you error step 5 tells there is no `wsl` command, you might need to restart your Windows and install all the updates.
  * Run `wsl -l -v` through powershell to check which version of WSL got installed
  * Create/Update credentials for the linux distribution: https://docs.microsoft.com/en-us/windows/wsl/user-support
* Install Java
  * `java -version` to check whether you have java already installed, if not then run these commands:
  * `sudo apt-get update`
  * `sudo apt install default-jdk` to install default JDK
    * If there is error about "dpkg", try `sudo dpkg --configure -a`
    * If there is Oracle configuration agreement came out, use "tab" key to choose "yes" to continue
  * `java -version`, `javac -version`
  * `readlink -f $(which java)` to find the java home location
    * After find that, `export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/bin/java`, java home path here depends on your own path
* Install Zookeeper
  * Find the latest stable release here: https://zookeeper.apache.org/releases.html
    * Copy downloaded file to linux subsystem: https://ridicurious.com/2018/10/18/2-ways-to-copy-files-from-windows-10-to-windows-sub-system-for-linux/
      * I was using `cp mnt/c/Users/wuhan/Downloads/apache-zookeeper-3.6.2-bin.tar.gz home/hanhan/Downloads/`
      * <b>Make sure to download the `bin.tar.gz` file, not the `tar.gz` file</b>
    * Installation Commands
      * `sudo tar -zxf home/hanhan/Downloads/apache-zookeeper-3.6.2-bin.tar.gz`
      * `sudo mv apache-zookeeper-3.6.2-bin /usr/local/zookeeper`
      * `cat > /usr/local/zookeeper/conf/zoo.cfg << EOF`
        * `tickTime=2000`
        * `dataDir=/var/lib/zookeeper`
        * `clientPort=2181`
        * `EOF`
      * `export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/bin/java`
    * `sudo /usr/local/zookeeper/bin/zkServer.sh start` to start zookeeper
      * Use `sudo /usr/local/zookeeper/bin/zkServer.sh start-foreground` to debug, there might be errors even though it's showing zookeeper has started
        * But when using this command, you cannot run stop command to stop zookeeper
    * `sudo /usr/local/zookeeper/bin/zkServer.sh stop` to stop zookeeper
    * To check whether zookeeper is running correctly
      * Method 1
        * Run `sudo /usr/local/zookeeper/bin/zkServer.sh status`, it's the same as `srvr` command
      * Method 2
        * `telnet localhost 2181`
        * `srvr`, this command lists full details of the serve. 
          * For all the zookeeper commands, check https://zookeeper.apache.org/doc/r3.4.8/zookeeperAdmin.html#sc_zkCommands
* Install Kafka Broker
  * Download Kafka from https://kafka.apache.org/downloads
  * `cp mnt/c/Users/wuhan/Downloads/kafka_2.13-2.6.0.tgz home/hanhan/Downloads/`
  * `sudo tar -zxf home/hanhan/Downloads/kafka_2.13-2.6.0.tgz`
  * `sudo mv kafka_2.13-2.6.0 /usr/local/kafka`
  * `mkdir /tmp/kafka-logs`
  * `export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/bin/java`
  * Start zookeeper first `sudo /usr/local/zookeeper/bin/zkServer.sh start`
  * Start kafka `sudo /usr/local/kafka/bin/kafka-server-start.sh -daemon /usr/local/kafka/config/server.properties`
  * Create and verify the topic
    * `sudo /usr/local/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test Created topic "test"`
    * `sudo /usr/local/kafka/bin/kafka-topics.sh --zookeeper localhost:2181 --describe --topic test`
  * Produce message tp test topic
    * `sudo /usr/local/kafka/bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test`
    * Ctrl + D to end
  * Consume message from test topic
    * `sudo /usr/local/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test --from-beginning`
    * Ctrl + C to end
  * Stop Kafka
    * `ps -ef` check whether both kafka server and zookeeper are running
    * `sudo /usr/local/kafka/bin/kafka-server-stop.sh` to stop kafka server
    * `sudo /usr/local/zookeeper/bin/zkServer.sh stop` to stop zookeeper
    * `ps -ef` to double check

#### Option 2 - Install on Windows
* This may bring some bugs that do not exist on Linux
* Install and config Java
  * Download and install JDK
  * Create a "user variable" named `JAVA_HOME` with the path of jdk, such as "C:\Program Files\Java\jdk-13.0.2"
  * Then edit the `Path` in system variable, by adding `%JAVA_HOME%\bin`
* Download Kafka from http://kafka.apache.org/downloads
  * Has to be the binary file, not the source file
  * Move the unzipped folder into `C:\`
* Open a powershell terminal to start `zookeeper`:
  * `cd C:\kafka_2.13-2.4.1\`
  * `bin/windows/zookeeper-server-start.bat C:\kafka_2.13-2.4.1\config\zookeeper.properties`
* After zookeeper started, open another powershell terminal to start Kafka:
  * `cd C:\kafka_2.13-2.4.1\`
  * `.\bin\windows\kafka-server-start.bat C:\kafka_2.13-2.4.1\config\server.properties`
* `Ctrl + C` to exit

### How to install Keras with Tensorflow on R Studio
* Have to install Keras with Tensorflow backend through Anaconda first, that's seems that only way R studio is trying to find available Keras & Tensorflow
* `devtools::install_github("rstudio/tensorflow")`  # make sure you have installed devtools
* `library("tensorflow")`
* `library("keras")`
* `reticulate::py_discover_config()`
* If `keras::is_keras_available()` will return TRUE, then you are good to go
### How to install Spark on Windows
* `pip install pyspark`, but only this step is far from being enough
* Download the lastest stable Spark release from http://spark.apache.org/downloads.html
  * Add SYSTEM environment variable similar to "SPARK_HOME=C:\somewhere\spark-3.0.0-bin-hadoop2.7"
* Download Java for windows from https://www.oracle.com/technetwork/java/javase/downloads/index.html
  * Add SYSTEM environment variable similar to "JAVA_HOM=C:\Program Files\Java\jdk-14.0.1"
* Download hadoop 2.7 from https://github.com/steveloughran/winutils
  * You can just keep folder "hadoop-2.7.1"
  * Add SYSTEM environment variable similar to "HADOOP_HOME=C:\somewhere\winutils-master\hadoop-2.7.1\bin"
* Add "%SPARK_HOME%\bin" to SYSTEM `Path`
* Create folder "C:\tmp\hive"
* Go you downloaded folder "hadoop-2.7.1\bin", run command "winutils.exe chmod 777 C:\tmp\hive"
  * If there is error saying missing MSVCR100.dll, try solutions here: https://www.drivereasy.com/knowledge/msvcr100-dll-missing-or-not-found-on-windows-solved/
    * I chose to install Visual C++ 2010: https://www.microsoft.com/en-hk/download/details.aspx?id=13523
* Restart your terminal
* Now you can go to spark home bin folder by typing `cd %SPARK_HOME%\bin`, try to run Spark
  * `spark-shell` will allow you write scala
  * `pyspark` will allow you write python, try `from pyspark.ml.fpm import PrefixSpan` to see whether it works
    * This function only became available from Spark 3 in python
  * Type `quit()` to quit the shell
* In fact, you can also just open jupyter notebook at anywhere, run `from pyspark.ml.fpm import FPGrowth` and see whether it works
  * But if you installed pyspark through conda virtual environment, do these:
    * `conda activate venv` to activate the virtual environemnt, "venv" is my virtual environment name
    * `pip install ipykernel`
    * `python -m ipykernel install --user --name conda_virtualenv --display-name "Python3 (venv)"` to add the venv kernal to Ipython
    * Then you can open your ipython at anywhere and use pyspark
* Reference: https://github.com/Cheng-Lin-Li/Spark/wiki/How-to-install-Spark-2.1.0-in-Windows-10-environment
#### NOTE
* When using Spark in Windows IPython, if you dind't terminate terminal and jupyter for a while, IPython could beahve abnormally, such as having java server errors
* To define spark, check https://github.com/hanhanwu/Hanhan-Spark-Python/blob/master/Spark2.0/how_to_define_spark.py
  * When there will be any error, you may need to adjust properties: http://spark.apache.org/docs/latest/configuration.html#available-properties
    
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
* `ss -tulpn` checks listening ports
  * `ss` is used to dump socket statistics and displays information in similar fashion (although simpler and faster) to netstat
* `ps -ef` checks current running processes
* Install `curl`: `sudo apt install curl`
  * You may get error saying "cannot get lock /var/lib/apt/lists/lock...", type `sudo rm /var/lib/apt/lists/lock` to solve the problem.
* Install `whois`
  * whois searches for an object in a WHOIS database. WHOIS is a query and response protocol that is widely used for querying databases that store the registered users of an Internet resource, such as a domain name or an IP address block, but is also used for a wider range of other information.
  * `sudo apt-get update`
  * `sudo apt-get install whois`
* To exit nslookup
  * `exit`
  * nslookup is built in many systems


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


[1]:https://github.com/hanhanwu/Hanhan-Spark-Python/tree/master/Spark2.0
[2]:https://help.github.com/en/github/importing-your-projects-to-github/adding-an-existing-project-to-github-using-the-command-line
[3]:https://www.youtube.com/watch?v=OA514h98bHE#:~:text=Go%20to%20control%20panel%5Csystem,options%20for%20better%20battery%20performance!&text=Disable%20%22windows%20search%22%20services%20(,consumes%20a%20lot%20of%20energy).&text=Please%20restart%20your%20system%20to%20apply%20the%20changes.
[4]:https://richpauloo.github.io/2018-05-16-Installing-the-R-kernel-in-Jupyter-Lab/

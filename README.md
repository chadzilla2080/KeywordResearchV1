# KeywordResearchV1
This is a keyword research script that helps you analyze a website's xml file to uncover content strategy and potential cpc strategy.

## Getting Started

These instructions will get your local machine setup to run Juypter and Anaconda to run this Notebook.

## What is a notebook? 

For those of you that are noobs, but search engine marketers struggling with Python, a notebook is a Juypter Python Env where you can have an interface to develop code. It's a very organized way of writing code and running the code line-by-line for less abstraction, more tangible engagement, and learning.

### Prerequisites

What things you need to install the software and how to install them

```
1. Install Python 3 Via Mac OSX

 a. To install Homebrew, open Terminal or your favorite OS X terminal emulator and run
 b. $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
 
This is a script above that you'll download via "curl" and what this script does is explain what changes it will make and prompt you before the installation begins. 

Once you’ve installed Homebrew, insert the Homebrew directory at the top of your PATH environment variable. You can do this by adding the following line at the bottom of your ~/.profile file

export PATH="/usr/local/opt/python/libexec/bin:$PATH"

** Noobs, you'll have to have some terminal skills, like knowing that ~ (tidal) is the "home path" on your computer system. If you're not sure about it, then you should really Googleit or take a fast course on Udemy or look for a free tutorial on Google.

 c. Now we can start to run brew to install Python 3
 d. $ brew install python
 
 *** This will take a few, so grab a beer!
 
 2. Install Pip
 
 Pip is a package manager for Python and you'll have to install libraies constantly while trying to run scrips that call on these Python libraries, Pip will install them and manage the dependcies for you.
 
 * Homebrew installs pip pointing to the Homebrew’d Python 3 for you.
 ** Run a test at command line to tell if you have Python3 installed, $ python3, this should launch an interpreter
 *** With the interpreter open run $ python --version, should print out the version of python installed by Brew.
 
 3. Download and Install Anaconda
 
 To install this, follow the instructions here: https://docs.anaconda.com/anaconda/install/mac-os/
 
 ** This is the link for a MAC OSX, if you have Winblows or Ubuntu, visit this link for your OS https://docs.anaconda.com/anaconda/install/

```

# KeywordResearchV1:: Script

This is a script meant to be ran with Juypter for educational purposes, if you run this via bash (bourne again shell aka terminal) you'll need to add print statements in between your panda data frames to be as verbose as you can via terminal enviornment. This is a way to see the results of what you're doing step by step. You can also code a delay so you can pause between major chucks of code.

For Example::

import advertools as adv
import plotly.graph_objects as go
import pandas as pd

safelite_generic = adv.sitemap_to_df('https://www.safelite.com/sitemap.xml')
safelite_images = adv.sitemap_to_df('https://www.safelite.com/image-sitemap.xml')

safelite = pd.concat([safelite_generic, safelite_images], ignore_index=True)

```
Here comes the print function, it takes the above line there and prints out the variable that we have the panda data frame

Many developers do this for debugging, get use to printing things out very powerful but entry level way to learn how to debug your shit!

```
print(safelite)

```
                                                   loc  \
0                             https://www.safelite.com/   
1            https://www.safelite.com/windshield-repair   
2     https://www.safelite.com/windshield-auto-glass...   
3     https://www.safelite.com/safelite-group-privac...   
4     https://www.safelite.com/about-safelite/safeli...   
...                                                 ...   
2088  https://espanol.safelite.com/resource-center/c...   
2089  https://espanol.safelite.com/resource-center/c...   
2090  https://espanol.safelite.com/resource-center/a...   
2091  https://espanol.safelite.com/resource-center/c...   
2092  https://www.safelite.com/resource-center/auto-...   

                       lastmod changefreq  priority  \
0    2019-10-24 00:00:00+00:00      daily       1.0   
1    2019-10-24 00:00:00+00:00      daily       0.9   
2    2019-10-24 00:00:00+00:00      daily       0.9   
3    2019-10-24 00:00:00+00:00      daily       0.9   
4    2019-10-24 00:00:00+00:00      daily       0.9   
...                        ...        ...       ...   
2088 2018-03-16 00:00:00+00:00      daily       0.5   
2089 2018-03-16 00:00:00+00:00      daily       0.5   
2090 2018-03-16 00:00:00+00:00      daily       0.5   
2091 2018-03-16 00:00:00+00:00      daily       0.5   
2092 2018-03-16 00:00:00+00:00      daily       0.5   

                                         sitemap image  
0           https://www.safelite.com/sitemap.xml   NaN  
1           https://www.safelite.com/sitemap.xml   NaN  
2           https://www.safelite.com/sitemap.xml   NaN  
3           https://www.safelite.com/sitemap.xml   NaN  
4           https://www.safelite.com/sitemap.xml   NaN  
...                                          ...   ...  
2088  https://www.safelite.com/image-sitemap.xml        
2089  https://www.safelite.com/image-sitemap.xml        
2090  https://www.safelite.com/image-sitemap.xml        
2091  https://www.safelite.com/image-sitemap.xml        
2092  https://www.safelite.com/image-sitemap.xml        

[2093 rows x 6 columns]

```

## Authors

**Chad Buie** 

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Big Thanks To Elias Dabbas and AdverTools Library :)
* https://github.com/eliasdabbas/advertools

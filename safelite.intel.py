# Pretty Standard Import These Libs, If You Get An Error Message It's Because You Have To Use Pip To Install Them
# To Run Pip, Go To Terminal, Run pip install advertools and repeat. 
# For Noobs Better To Run This Line By Line Via Anaconda and Juypter

import advertools as adv
import plotly.graph_objects as go
import pandas as pd

safelite_generic = adv.sitemap_to_df('https://www.safelite.com/sitemap.xml')
safelite_images = adv.sitemap_to_df('https://www.safelite.com/image-sitemap.xml')

safelite = pd.concat([safelite_generic, safelite_images], ignore_index=True)

# Debug, See Your Data Frame Via Command Line aka Terminal

print(safelite)

# Here I Set A Column To Data Frame and Split The Url String at Position Three Of The Url To Gather Keyword Data

safelite['sitemap_cat'] = safelite['loc'].str.split('/').str[4]

# Print Out Small Sample, Esp If You Are Dealing With A Large Data Set

safelite.sample(1000)

# Outbrain-Click-Prediction
<hr>

![Python](https://img.shields.io/badge/<Python>-<3.7>-<brightgreen>.svg)
![Jupyter](https://img.shields.io/badge/Jupyter-v1.0.0-blue.svg)


✨ Can you predict which recommended content each user will click?



**Author** : Hyuntaek Lim, luckyquit49@gmail.com

Supervisor : Na, In Seop, ypencil@hanmail.net

Starting Project : 2019.1.8



# Project summary
<hr>

Outbrain Click Prediction Overview : https://www.kaggle.com/c/outbrain-click-prediction

Outbrain-Click-Predcition Github : https://github.com/bajajsweta/Outbrain-Click-Prediction



# Data Sources file descriptions
<hr>

**page_views.csv** is a the log of users visiting documents. To save disk space, the timestamps in the entire dataset are relative to the first time in the dataset. If you wish to recover the actual epoch time of the visit, add 1465876799998 to the timestamp.

- uuid
- document_id
- timestamp (ms since 1970-01-01 - 1465876799998)
- platform (desktop = 1, mobile = 2, tablet =3)
- geo_location (country>state>DMA)
- traffic_source (internal = 1, search = 2, social = 3)

**clicks_train.csv** is the training set, showing which of a set of ads was clicked.

- display_id
- ad_id
- clicked (1 if clicked, 0 otherwise)

**clicks_test.csv** is the same as clicks_train.csv, except it does not have the clicked ad. This - is the file you should use to predict. Each display_id has only one clicked ad. Note that test set contains display_ids from the entire dataset timeframe. Additionally, the public/private sampling for the competition is uniformly random, not based on time. These sampling choices were intentional, in spite of the possibility that participants can look ahead in time.

**sample_submission.csv** shows the correct submission format.

**events.csv** provides information on the display_id context. It covers both the train and test set.

- display_id
- uuid
- document_id
- timestamp
- platform
- geo_location

**promoted_content.csv** provides details on the ads.

- ad_id
- document_id
- campaign_id
- advertiser_id

**documents_meta.csv** provides details on the documents.

- document_id
- source_id (the part of the site on which the document is displayed, e.g. edition.cnn.com)
- publisher_id
- publish_time

**documents_topics.csv**, **documents_entities.csv**, and **documents_categories.csv** all provide information about the content in a document, as well as Outbrain's confidence in each respective relationship. For example, an entity_id can represent a person, organization, or location. The rows in documents_entities.csv give the confidence that the given entity was referred to in the document.



# Examples
<hr>

```python
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import gc # We're gonna be clearing memory a lot
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

p = sns.color_palette()

print('# File sizes')
for f in os.listdir('./Desktop/openSW/input/'):
    if 'zip' not in f:
        print(f.ljust(30) + str(round(os.path.getsize('./Desktop/openSW/input/' + f) / 1000000, 2)) + 'MB')
```



#  Requirements
<hr>

- **[Python 3.7](https://www.python.org/)**

- **Python library**
    ```
    pip install [lib_name] or
    pip3 install [lib_name]
    ```

- **[Jupyter Notebook](https://jupyter.org/)**
    ```
    pip install jupyter or 
    pip3 install jupyter
    ```

- **[Outbrain-Click-Prediction Algorithm](https://github.com/bajajsweta/Outbrain-Click-Prediction)**
    ```
    https://github.com/bajajsweta/Outbrain-Click-Prediction.git
    ```

- **[Outbrain Click Prediction Data Sources](https://www.kaggle.com/c/outbrain-click-prediction/data)** for Windows
    ```
    kaggle competitions download -c outbrain-click-prediction
    ```




# License
<hr>

**Outbrain Click Prediction** is under GNU General Public License v3.0. See the [LICENSE](LICENSE) file for more info.
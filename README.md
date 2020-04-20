# Kubios Data Loading 
This package will allow users to import pre-analysed Kubios text files into python. 
This transforms the raw text file into a pandas data frame which can be used in further analysis or machine learning. 

## Usage 
import the package and with the final function of the class you will be able to extract all different segments of the 
kubios data-analysis in a dict. 

```python
from KubiosDataloader import KubiosDataLoader

data_loader = KubiosDataLoader(kubios_data = "filename.txt") #insert file location of the kubios text file
kubios_dict = KubiosDataLoader.kubios_data_extraction() # returns dictionary with data frames of every section in the kubios file
```
## To do 
- Optimizing data frame sections besides the time-varying data frame
- Write more tests 

##License 
GNU GPLv3 
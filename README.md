# data_explore

Fast and visual EDA (Exploratory Data Analysis) package

## How to install my package

For the moment, this package is only available on github. For the
```bash
pip install git+https://github.com/petoulemonde/data_explore
```

## How to use my package ?

`data_explore` package can be used to make beautiful and powerfull dataset descirption, as follows:

```python
from data_explore import data_explore

# For example I will use titanic dataset from seaborn
from seaborn import load_dataset
titanic = load_dataset("titanic") # Lod titanic dataset from seaborn package

# My package : 
t = data_explore(titanic) # Create data_explore object with titanic dataset
t = date_explore(titanic, y ="who") # For further description, specify variable y

t.glimpse() # General description of the dataset
t.num_var() # Description of numeric variables (numerically and graphically)
t.cat_var() # Description of cateogircal variables (numerically and graphically)
t.mis_val() # Description of missing values of the dataset

t.update(titanic_modified) # Updating dataset in the data_explore object. Usefull to update dataset after modification.

# For help:
help(data_explore) # General help. 
help(data_explore.glimpse) # Help for glimpse function
```

## Contributing

You are free to fork the project, or to propose modification by email or other ways.
My email is: pierre-etienne.toulemonde@outlook.com .

## Licence

`data_explore` was created by Pierre-Etienne Toulemonde. It is licensed under the terms
of the MIT license.

-------------------------------------------------------------------------------

# Logs

## Version 1.0.0 :

- Creation of project

- Importation of source code. Functions:
	- *glimpse()* : global description of dataset

	- *num_var()*: description of numeric variables (numerically and graphically)

	- *cat_var()*: description of categorical variables (numerically and graphically)

	- *update()*: update dataset in data_explore object

	- *mis_val()*: Description of missing values in dataset

### Suggested Improvement: 

- *num_var()*: add a playground of 2 * 2 scatter plots with for each graph the choice of x, y, size and color variables

- *cat_vat()*: add *var* argument to choice order of variables in pie plot and alluvial plot

- *mis_val()*: add a heatmap of missing value patterns and a histogram of missing values per variable in the data set
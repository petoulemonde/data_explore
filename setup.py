from setuptools import *

# Rédaction du setup.py : https://docs.python.org/fr/3/distutils/setupscript.html
# AIde pour mieux comprendre le setup : https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/
# aller plus loin dans l'arborescence : https://docs.python.org/fr/3/distutils/setupscript.html
# https://stackoverflow.com/questions/1471994/what-is-setup-py

setup(
    name = "data_explore", # Name of package
    description = "data_explore is a EDA python package.",
    author = "Pierre-Etienne Toulemonde",
    author_email = "pierre-etienne.toulemonde@outlook.com",
    maintainer = "Pierre-Etienne Toulemonde",
    py_modules = ["data_explore"],
    # packages = ["data_explore", "numpy", "pandas", "plotly.express", "plotly.graph_objects", "tableone"],
    url = "https://github.com/petoulemonde/data_explore",
    version = "1.0.1",

    # install_requires=["plotly.express", "plotly.graph_objects", "numpy", "pandas", "tableone"],
    install_requires=["plotly", "numpy", "pandas", "tableone"]
)


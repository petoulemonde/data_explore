import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd
from tableone import TableOne
import math

# if __name__ == "__main__":
#    print(bonjour("Joe"))
# S'éxcute si le script est appelé comme script, et non comme module
# python <file>.py -> script
# import <file> -> module

class data_explore:
  """Class docstring"""

  def __init__(self, dataset, y = " ") :
    """__init__ docstring"""
    
    if type(dataset) == np.ndarray : 
      self.dataset = pd.DataFrame(dataset)
    elif type(dataset) == pd.DataFrame :
      self.dataset = dataset
    else : 
      print("ERROR! Type of dataset is not np.array or pd.DataFrame.")

    self.y = y

# ------------------------------------------------------------------------------
  def update(self, dataset, y = " ") :
    """This function display a quick sum up of the dataset.
    
    The glimpse function makes a global summary of the dataset. This summary is composed of 5 description elements: 
    1/ shape of dataset, with name and type of variables,
    2/ The first 20 lines of the dataset,
    3/ the list of numerical variables of the dataset, with a numerical summary,
    4/ The list of categorical variables, with a quick numerical summary,
    5/ A table one of the dataset.

    Parameters
    ----------
    dataset : np.array or pd.DataFrame
      Dataset contained in the data_explore object.
    y : str, optional
	    Categorical variable of the dataset. The description of the dataset will be based on y.
    
    Returns
    -------
    data_explore object, with dataset updated
    """

    if type(dataset) == np.ndarray : 
      self.dataset = pd.DataFrame(dataset)
    elif type(dataset) == pd.DataFrame :
      self.dataset = dataset
    else : 
      print("ERROR! Type of dataset is not np.array or pd.DataFrame.")

    if y != " ":
      self.y = y
# ------------------------------------------------------------------------------
  def glimpse(self, y = " ", exec = [1, 2, 3, 4, 5]) :
    """This function display a quick sum up of the dataset.
    
    The glimpse function makes a global summary of the dataset. This summary is composed of 5 description elements: 
    1/ shape of dataset, with name and type of variables,
    2/ The first 20 lines of the dataset,
    3/ the list of numerical variables of the dataset, with a numerical summary,
    4/ The list of categorical variables, with a quick numerical summary,
    5/ A table one of the dataset.

    Parameters
    ----------
    y : str, optional
	    Categorical variable of the dataset. The description of the dataset will be based on y.
    exec : list, optional
      The function is divided into 5 steps. The exec parameter specifies the steps to be displayed.

    Returns
    -------
    No object returned
    """

    exec = [str(x) for x in exec]

    if y != " ":
      y_used = y
    else : 
      y_used = self.y
    
    print(" ---------- Start of the general description of the dataset ---------- \n")

    if "1" in exec : 
      # Shape
      print("Shape of dataset is : " + str(self.dataset.shape) + " (" + str(self.dataset.shape[0]) + " lines, " + str(self.dataset.shape[1]) + " columns) .\n")
      print("About varaibles of the dataset : \n")
      print(self.dataset.info())
      print("\n")
    
    if "2" in exec : 
      # Head
      print("The first lines of your dataset are : ")
      print(self.dataset.head(20))
      print("\n")

    if "3" in exec : 
      # Numeric variables
      df = self.dataset[self.dataset.select_dtypes(include = np.number).columns.tolist()]
      print("Numeric coluns are : " + str(df.columns.tolist()))
      print(self.dataset.describe())
      print("\n")

    if "4" in exec : 
      # Categorical variables
      df = self.dataset.drop(self.dataset.select_dtypes(include = np.number).columns.tolist(), axis = 1)

      print("Categorical columns are : " + str(df.columns.tolist()))
      print(self.dataset.drop(self.dataset.select_dtypes(include = np.number).columns.tolist(), axis=1).describe())
      print("\n")

    if "5" in exec : 
      # table one
      print("The table one about this dataset is : ")
      columns = self.dataset.columns.tolist()

      if y_used != " " : 
        print("y variable is : '" + y_used + "' :")
        print(TableOne(self.dataset, columns, groupby = y_used).tabulate(tablefmt = "github"))
      else : 
        print(TableOne(self.dataset, columns).tabulate(tablefmt = "github"))
      print("\n")

    print("\n ---------- End of general description of the dataset ---------- \n\n")

# ------------------------------------------------------------------------------

  def num_var(self, y = " ", exec = [1, 2, 3, 4]):
    exec = [str(x) for x in exec]

    if y != " ":
      y_used = y
    else : 
      y_used = self.y

    print(" ---------- Start of the description of the numerical variables ---------- ")

    if y_used == " " :
      # Numeric description

      if "1" in exec : 
        df = self.dataset[self.dataset.select_dtypes(include = np.number).columns.tolist()]
        print("Numeric columns are : " + str(df.columns.tolist()) + ".\n")
        print(df.describe())

      if "2" in exec : 
        df = self.dataset[self.dataset.select_dtypes(include = np.number).columns.tolist()]
        df_melted = df.melt()
        fig = px.box(df_melted,
                    x = "variable",
                    y = "value", 
                    color = "variable",
                    title = "Description of numeric variables")
        fig.show()

      if "3" in exec : 
        df = self.dataset[self.dataset.select_dtypes(include = np.number).columns.tolist()]
        
        fig = px.scatter_matrix(df)
        fig.show()

    else : 
      if "1" in exec :
        df = self.dataset[self.dataset.select_dtypes(include = np.number).columns.tolist() + [y_used]]
        print("Numeric columns are : " + str(df.columns.tolist()) + ".\n")
        print(df.describe())
      
      if "2" in exec : 
        df = self.dataset[self.dataset.select_dtypes(include = np.number).columns.tolist() + [y_used]]
        df_melted = df.melt()
        fig = px.box(df_melted,
                    x = "variable",
                    y = "value", 
                    color = "variable",
                    title = "Description of numeric variables")
        fig.show()

      if "3" in exec : 
        df = self.dataset[self.dataset.select_dtypes(include = np.number).columns.tolist() + [y_used]]
        
        fig = px.scatter_matrix(df, color=y_used, symbol = y_used)
        fig.show()
        
        # for i in self.dataset[y_used].unique() : 
        #   print("\nFor " + y_used + " = '" + i +"': ")
        #  print(self.dataset[self.dataset[y_used] == i].describe())

      if "4" in exec : 
        if len(self.dataset.columns) == 1 : 
          fig = px.box(df, x = y_used)
          fig.show()
        
        else : 
          df_melted = df.melt(id_vars = [y_used])
          fig = px.box(df_melted,
                      x = "variable", 
                      y = "value", 
                      color = "variable",
                      title = "Description of numeric variables",
                      facet_col = y_used)
          fig.show()
      
    print("\n ---------- End of of the description of the numerical variables ---------- \n\n")

# ------------------------------------------------------------------------------

  def cat_var(self, exec = [1, 2, 3, 4]) :
    exec = [str(x) for x in exec]

    print(" ---------- Start of the description of the categorical variables ---------- \n")

    if "1" in exec : 
      # List of catagorical variables
      df = self.dataset.drop(self.dataset.select_dtypes(include = np.number).columns.tolist(), axis = 1)
      print("Categorical columns are : " + str( df.columns.tolist() ) )
      print("\n")
      # Variable per variable description
      print(self.dataset.drop(self.dataset.select_dtypes(include = np.number).columns.tolist(), axis = 1).describe())

    if "2" in exec : 
      df_unmelt = self.dataset.drop(self.dataset.select_dtypes(include = np.number), axis = 1)
      df = df_unmelt.melt()
      n_rows = math.trunc(len(df_unmelt.columns)/2) + len(df_unmelt.columns)%2 
      fig = make_subplots(rows = n_rows, 
                          cols = 2,
                          subplot_titles= pd.unique(df.variable.apply(lambda x: str("Variable: " + str(x)))) )

      for i in range(1, n_rows+1) :
        for j in range(1, 3) : 
          fig.add_trace(
              go.Histogram(x =  df[df.variable == pd.unique(df.variable)[i+j-2]].value,
                          name = str( pd.unique( df[df.variable == pd.unique(df.variable)[i+j-2]].variable ) ) 
                          ), 
              # layout = go.Layout(title=go.layout.Title(text= str( pd.unique( df[df.variable == pd.unique(df.variable)[i+j-2]].variable ) ) ) ), 
              row = i, col = j)
      fig.show()

    if "3" in exec : 
      # Sunburst plot
      print("Pie plot with all categorical variables : \n")
      df_combinations = (
          self.dataset.groupby(self.dataset.drop(self.dataset.select_dtypes(include = np.number).columns.tolist(), axis = 1).columns.tolist() )
          .size()
          .reset_index()
          .rename(columns = {0: "count"} ) )

      fig = px.sunburst(
          df_combinations,
          path = self.dataset.drop(self.dataset.select_dtypes(include = np.number).columns.tolist(), axis = 1).columns.tolist(),
          values = "count", 
          title = "Sunburst plot"
          # height = 800
      )
      fig.show()

    if "4" in exec : 
      # Alluvial plot
      print("Alluvial plot for all categorical variables : \n")
      
      if self.y != " " :
        list_var = titanic.drop(titanic.select_dtypes(include = np.number).columns.tolist(), axis = 1).columns.tolist()
        list_class = list_var

        for i in range(0, len(list_var)) :
          var = list_var[i]
          list_class[i] = go.parcats.Dimension(values = titanic[var], label = i )
        
        fig = go.Figure(data = [
          go.Parcats(dimensions = list_class) ] )
        fig.show()
      
      else : # OK
        fig = px.parallel_categories(self.dataset.drop(self.dataset.select_dtypes(include = np.number).columns.tolist(), axis = 1))
        fig.show()

    print(" -------- End of the description of the categorical variables ---------- ")

# ------------------------------------------------------------------------------
  def mis_val(self, exec = [1, 2]) :
    exec = [str(x) for x in exec]
    
    print(" -------- Start of the description missing values ---------- ")

    if '1' in exec : 
      print("Missing values row by rows : ")
      print("White correspond to available/existing missing values, gray to missing values. \n\n")

      my_scale = [('rgb(150, 150, 150)'),
            ('rgb(255, 255, 255)')]

      fig = px.imshow(self.dataset.isnull(),
                      color_continuous_scale = my_scale,)
      fig.layout.coloraxis.showscale = False
      fig.show()

    if '2' in exec :
      print("Pattern of missing valeus in the dataset : ")
      # Heatmap
      df = self.dataset.isnull().groupby(self.dataset.columns.tolist(), as_index = False).size().sort_values("size").reset_index().drop("index", axis=1).set_index("size")
      df = df.astype(int).reset_index()
      df["size"] = df["size"].apply(lambda x: "n = " + str(x))
      # df = df.melt("size")

      my_scale = [('rgb(51, 51,255)'),
            ('rgb(255,51, 51)')]
      # rgb color : https://www.rapidtables.com/web/color/RGB_Color.html

      fig1 = go.Figure(
        data=go.Heatmap(x = df.drop("size", axis = 1).columns.tolist(),
                        y = pd.Series(df["size"]).tolist(),
                        z=df.drop("size", axis = 1).values,
                        # colorscale = 'Bluered',
                        colorscale = my_scale,
                        hovertemplate = 'Variable : %{x} <br>Number of rows concerned : %{y}<br>Is missing ? (0: False/ 1: True) : %{z}<extra></extra>',
        )
      )
      fig1.update_traces(showscale=False)

      # Histogram
      dt = self.dataset.isnull().sum().sort_values()
      dt[dt == 0] = 0.001
      dt = dt.append(pd.Series(self.dataset.shape[0], index = ["n_total_rows"]))

      fig2 = px.bar(x = dt.index, y = dt.values, text = dt.values)

      # 2 plots together
      def quick_plot(n, nrows, ncols, *args):
        import plotly.subplots as sp
        from plotly.subplots import make_subplots

        fig=[]
        fig=[] #list to store figures
        for arg in args:
            fig.append(arg)

        fig_traces={}

        # Appending the traces of the figures to a list in fig_traces dictionary
        for i in range(n):  
          fig_traces[f'fig_trace{i}']=[]

          for trace in range(len(fig[i]["data"])):
              fig_traces[f'fig_trace{i}'].append(fig[i]["data"][trace])

        #Creating a subplot
        combined_fig = sp.make_subplots(rows = nrows, cols = ncols)

        #Appending the traces to the newly created subplot
        i=0
        for a in range(1, nrows+1):
            for b in range(1, ncols+1):
                for traces in fig_traces[f"fig_trace{i}"]:
                    combined_fig.add_trace(traces, row=a, col=b)
                i+=1

        return combined_fig
        # link: https://stackoverflow.com/questions/56727843/how-can-i-create-subplots-with-plotly-express

      f = quick_plot(2, 1, 2, fig1, fig2)
      f.show()

    print(" -------- End of the description missing values ---------- ")
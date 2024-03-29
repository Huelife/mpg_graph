#mpg_graph.py: Graphing mpg trend of two cars over time

import pandas as pd
import matplotlib.pyplot as plt

#mpg over time data for camry and avalon
camry_df = pd.Series({
  "04/12/18":18.3,
  "04/14/18":21.6,
  "04/20/18":18.6,
  "04/27/18":16.1,
  "05/17/18":17.8,
  "06/01/18":18.6,
  "06/24/18":19.0,
  "07/13/18":18.6,
  "08/03/18":18.7,
  "08/24/18":18.8,
  "10/07/18":18.6,
  "10/29/18":17.9,
  "11/10/18":19.1,
  "11/30/18":18.0,
  "12/11/18":14.3,
  "12/17/18":16.0,
  "12/26/18":19.3,
  "01/04/19":18.7,
  "01/17/19":17.6,
  "01/24/19":19.2,
  "01/31/19":19.7,
  "02/13/19":21.6,
  "02/28/19":22.9,
  "03/13/19":22.3,
  "04/02/19":21.2,
  "04/17/19":20.9,
  "05/02/19":22.5,
  "05/21/19":22.1,
  "06/12/19":22.9,
})

avalon_df = pd.Series({
  "04/12/18":None,
  "05/17/18":None,
  "06/01/18":None,
  "07/13/18":None,
  "08/03/18":None,
  "08/24/18":None,
  "10/07/18":None,
  "10/29/18":None,
  "11/17/18":22.5,
  "12/02/18":21.4,
  "12/09/18":23.4,
  "02/01/19":27.9,
  "02/05/19":19.7,
  "02/11/19":22.8,
  "02/17/19":21.3,
  "02/22/19":23.6,
  "02/28/19":21.7,
  "03/08/19":21.9,
  "03/14/19":21.7,
  "03/19/19":22.5,
  "03/28/19":20.7,
  "04/07/19":21.3,
  "04/13/19":22.7,
  "04/18/19":22.1,
  "04/24/19":22.2,
  "04/28/19":23.4,
  "05/19/19":21.5,
  "05/26/19":21.4,
  "06/12/19":None,
})

camry_df.plot()
avalon_df.plot()
plt.title("Car MPG (Miles Per Gallon) Over Time")
plt.legend(["1993 Toyota Camry","2002 Toyota Avalon"])
plt.xlabel("Date")
plt.ylabel("MPG (Miles Per Gallon)")
plt.show()

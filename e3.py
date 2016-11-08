import pandas as pd
import matplotlib.pyplot as plt

df_list = []
for i in range(1924,2013,4):
# Given scripts for read_csv().
    csv_file = str(i) +".csv"
    header = pd.read_csv(csv_file, nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()
    df = pd.read_csv(csv_file, index_col = 0,
        thousands = ",", skiprows = [1])
    df.rename(inplace = True, columns = d) # rename to democrat/republican
    df.dropna(inplace = True, axis = 1)    # drop empty columns
    df["Year"] = i
    #df["Republican Share"] = df["Republican"]/df["Total Votes Cast"]
    df_list.append(df[["Democratic", "Republican", "Total Votes Cast", "Year"]])

DF = pd.concat(df_list)
DF["Republican Share"] = DF["Republican"]/DF["Total Votes Cast"]
# Save the plot as png.
DF.loc[["Accomack County"]].plot(kind = "line", x = "Year", y = "Republican Share")
plt.savefig("accomack.png")

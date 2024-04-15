import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv("data/companydata.csv")
    data_selection = data[['Dept', 'Sold', 'Returned', 'Ordered']]
    data_summary = data_selection.groupby(["Dept"]).sum()
    print(data_summary)
import pandas as pd

if __name__ == "__main__":
    data = pd.read_csv("data/companydata.csv")
    data_selection = data[['Dept', 'Sold', 'Returned', 'Ordered']]
    data_summary = data_selection.groupby(["Dept"]).sum()
    data_summary.to_csv("data/dashboarddata.csv", index=True, header=True)
    print(data_summary)
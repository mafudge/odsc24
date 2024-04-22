import pandas as pd

if __name__ == "__main__":
    print("Reading Source...")
    data = pd.read_csv("data/companydata.csv")
    
    print("Transforming Source to Target...")
    data_selection = data[['Dept', 'Sold', 'Returned', 'Ordered']]
    data_summary = data_selection.groupby(["Dept"]).sum()

    print("Writing Target...")    
    data_summary.to_csv("data/dashboarddata.csv", index=True, header=True)
    print(data_summary)
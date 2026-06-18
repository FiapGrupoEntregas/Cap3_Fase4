import pandas as pd

def main():
    df = pd.read_csv('seeds_dataset.txt', sep=r'\s+')

    print(df.head())

if __name__ == "__main__":
    main()
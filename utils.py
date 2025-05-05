def load_data():
    """Load the Titanic dataset into a Pandas DataFrame with only male passengers."""
    df = pd.read_csv("/workspaces/git_kata/data/titanic.csv")
    return df[df["Sex"] == "male"]
import pandas as pd

def clean_data(df):
    """
    Clean the given DataFrame by:
    - Dropping rows with missing values
    - Converting all string (categorical) columns to lowercase
    """
    df = df.dropna()

    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.lower()

    return df


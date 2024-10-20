# Document here

import os
import pandas as pd
import matplotlib.pyplot as plt

def load_data_from_folder(folder_path):
    """
    Load all CSV files from the given folder without headers and return a combined DataFrame.
    """
    all_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.csv')]
    df_list = [pd.read_csv(file, header=None) for file in all_files]  # Load without headers
    combined_df = pd.concat(df_list, ignore_index=True)
    return combined_df

def calculate_correct_answer_frequencies(df):
    """
    Calculate the frequency of correct answers (A, B, C, D).
    Assumes the correct answer is in the last column.
    """
    # Access the last column by index
    correct_answers = df.iloc[:, -1].astype(str).str.strip()  # Ensure all values are strings and strip whitespace

    # Print the first 20 values of the last column to understand what kind of data we have
    print("First 20 values in the last column:")
    print(correct_answers.head(20))

    # Filter only valid answer choices (A, B, C, D)
    valid_answers = correct_answers[correct_answers.isin(['A', 'B', 'C', 'D'])]
    print("Filtered valid answers (A, B, C, D):")
    print(valid_answers.head(20))  # Print the first 20 filtered values

    # Calculate the frequency of valid answers
    answer_counts = valid_answers.value_counts()
    return answer_counts





def visualize_answer_frequencies(answer_counts):
    """
    Create a bar chart to visualize the frequency of correct answers.
    Enhanced version with data labels and custom colors.
    """
    plt.figure(figsize=(10, 6))
    bars = answer_counts.plot(kind='bar', color=['skyblue', 'lightgreen', 'salmon', 'gold'], legend=False)
    plt.xlabel('Answer Options')
    plt.ylabel('Frequency of Correct Answers')
    plt.title('Frequency of Correct Answers (A, B, C, D)')
    plt.xticks(rotation=0)

    # Add data labels to each bar
    for bar in bars.patches:
        bars.annotate(format(bar.get_height(), '.0f'),
                      (bar.get_x() + bar.get_width() / 2, bar.get_height()),
                      ha='center', va='bottom',
                      fontsize=10, color='black', xytext=(0, 5),
                      textcoords='offset points')
    
    plt.tight_layout()  # Adjust the layout to fit labels properly
    plt.show()
    
def identify_correct_answer_column(df):
    """
    Iterate through each column and print unique values to identify which column
    contains the correct answers (A, B, C, D).
    """
    for column in df.columns:
        unique_values = df[column].dropna().unique()
        print(f"Column '{column}' unique values: {unique_values[:10]}")  # Show up to 10 unique values to check



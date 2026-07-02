import pandas as pd

def calculate_correlation(input_file_path, output_file_path):
    # Load the Excel file
    df = pd.read_excel(input_file_path)
    # Convert 'yes'/'no' values to 1 and 0
    df.replace({'yes': 1, 'no': 0}, inplace=True)
    df.replace({'furnished':2,  'unfurnished':1, 'semi-furnished':0}, inplace=True)
    
    print(df.head(5))
    
    # Calculate the correlation matrix
    correlation_matrix = df.corr()
    
    # Save the correlation matrix to a new Excel file
    correlation_matrix.to_excel(output_file_path)
    
    print(f"Correlation matrix has been saved to {output_file_path}")

# Example usage
input_file = 'Housing.xlsx'  # Replace with your input file path
output_file = 'Housing_correl.xlsx'  # Replace with your desired output file path

calculate_correlation(input_file, output_file)

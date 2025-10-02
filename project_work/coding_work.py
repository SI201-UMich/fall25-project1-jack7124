### SI 201 Project 1: CSV
### Name: Jackson Miller
### Uniqname: miljack
### UMID: 7012 3312
### Collaborators: Vittorio Centore and ChatGPT 5.0 and Gemini Pro
### Gen AI Statement: Used ChatGPT for general potential function outlines for inputs, outputs, and usage,
### , and for our flowchart ideas. We used Gemini and ChatGPT collectively for general debugging help.





import csv



def load_data(csv_file: str):
    """
    This is a combined function that both imports the csv file 
    and creates a dictionary for each line


    using try except since we are reading in files 
    """
    data = []
    with open(csv_file, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:


            ## reading in each row for our columns. While the columns below may not be our
            ## selected ones, we have to read them in correctly or they return none
            ## so we read in by float or int depending on context
            ## Using try except because of file opening risk 
            if row.get("bill_length_mm"):
                try:
                    row["bill_length_mm"] = float(row["bill_length_mm"])
                except ValueError:
                    row["bill_length_mm"] = None

            if row.get("bill_depth_mm"):
                try:
                    row["bill_depth_mm"] = float(row["bill_depth_mm"])
                except ValueError:
                    row["bill_depth_mm"] = None

            if row.get("flipper_length_mm"):
                try:
                    row["flipper_length_mm"] = int(row["flipper_length_mm"])
                except ValueError:
                    row["flipper_length_mm"] = None

            if row.get("body_mass_g"):
                try:
                    row["body_mass_g"] = int(row["body_mass_g"])
                except ValueError:
                    row["body_mass_g"] = None


            ### For rows that don't need int or float conversion, just append 
            data.append(row)
    return data


def calculate_average_body_mass(data):
    """
    Calculates average body mass for each penguin species.
    INPUT: data (list of dicts)
    OUTPUT: avg_body_mass (dict {species: avg_mass})
    """
    pass


def select_heavy_bills(data):
    """
    Filters penguins with body mass > 3500g 
    and calculates average bill length.
    INPUT: data (list of dicts)
    OUTPUT: avg_bill_length (float)
    """
    pass


def find_upper_quartile_long_bills(data):
    """
    Identifies penguins in upper 25% of body mass 
    that also have a bill length > 42 mm.
    INPUT: data (list of dicts)
    OUTPUT: num_upper_quartile_long_bills (int)
    """
    pass


def find_heavy_quartile_long_bills(data):
    """
    Counts penguins with body mass > 4000g.
    INPUT: data (list of dicts)
    OUTPUT: count (int)
    """
    pass


def find_heavy_gentoo_count(data):
    """
    Counts total Gentoo penguins with body mass > 4000g.
    INPUT: data (list of dicts)
    OUTPUT: count (int)
    """
    pass


def main():
    """
    Calls the other functions in a logical sequence.
    INPUT: None
    OUTPUT: None
    """

    file_path = "project_work/penguins.csv"

    # Confirms the file path is correct          
    print(">>> Looking for:", file_path)    
    
    csv_data = load_data(file_path)

    # confirming csv_data produces desired output 
    print(">>> Rows loaded:", len(csv_data))
    for row in csv_data:
        print(row)


    # for future notice 
    '''
    find_heavy_gentoo_count(csv_data)
    for d in csv_data:
        if d["species"] == 
    '''




main()
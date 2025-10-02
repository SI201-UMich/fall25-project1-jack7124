import csv

def import_csv(file_path):
    data =[]
    with open(file_path, newline='') as csvfile:
        file_reader = csv.reader(csvfile)
        for row in file_reader:
            data.append(row)
    return data



def load_data(csv_file: str):
    """
    Reads CSV into a suitable data structure (list of dicts).
    INPUT: csv_file (str)
    OUTPUT: data (list of dicts)
    """
    pass


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
    print(">>> Entered main()")             # confirm main is running
    print(">>> Looking for:", file_path)    # confirm where it thinks the file is
    
    csv_data = import_csv(file_path)
    print(">>> Rows loaded:", len(csv_data)) # confirm if anything was read
    
    for row in csv_data:
        print(row)


main()
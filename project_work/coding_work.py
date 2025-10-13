### SI 201 Project 1: CSV
### Name: Jackson Miller
### Uniqname: miljack
### UMID: 7012 3312
### Collaborators: Vittorio Centore and ChatGPT 5.0 and Gemini Pro
### Gen AI Statement: Used ChatGPT for general potential function outlines for inputs, outputs, and usage,
### , and for our flowchart ideas. We used Gemini and ChatGPT collectively for general debugging help.





import csv
import unittest



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
    OUTPUT: avg_body_mass (dict {species: avg_mass}) to a new file
    """

    avg_body_mass = {}
    for row in data:
        row_species = row["species"]
        row_mass = row["body_mass_g"]
        if row_mass is None:
            row["body_mass_g"] = 0
        if row_species is None:
            row["species"] = "Unknown"
        

        ## Using dict to store mass for each species 

        if row_species not in avg_body_mass:
            avg_body_mass[row_species] = {}
            avg_body_mass[row_species] = 0
        
        avg_body_mass[row_species] += row_mass

    
    for species in avg_body_mass:
        count = sum(1 for row in data if row["species"] == species and row["body_mass_g"] is not None)
        if count > 0:
            avg_body_mass[species] /= count
        else:
            avg_body_mass[species] = 0
    

    #with open("average_body_mass.txt", "w") as f:
       # for species in avg_body_mass.items():
        #    f.write(f"{species[0]}: {species[1]:.2f} g\n")

    print(">>> Avg body mass:", avg_body_mass)
    return avg_body_mass

    


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


class test_work(unittest.TestCase):
    def test_load_data(self):
        data = load_data("project_work/penguins.csv")
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        self.assertIsInstance(data[0], dict)
        self.assertEqual(set(data[0].keys()), {'', 'species', 'island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex', 'year'})

    def test_calculate_average_body_mass(self):
        data = [
            {"species": "Adelie", "body_mass_g": 3700},
            {"species": "Adelie", "body_mass_g": 3800},
            {"species": "Chinstrap", "body_mass_g": 3500},
            {"species": "Chinstrap", "body_mass_g": 3000},
            {"species": "Gentoo", "body_mass_g": 5000},
        ]
        avg_body_mass = calculate_average_body_mass(data)
        self.assertAlmostEqual(avg_body_mass["Adelie"], 3750.0)
        self.assertAlmostEqual(avg_body_mass["Chinstrap"], 3250.0)
        self.assertAlmostEqual(avg_body_mass["Gentoo"], 5000.0)



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







if __name__ == "__main__":
    main()  # optional: runs your main function
    unittest.main()




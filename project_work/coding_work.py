### SI 201 Project 1: CSV
### Name: Jackson Miller
### Uniqname: miljack
### UMID: 7012 3312
### Collaborators: Vittorio Centore and ChatGPT 5.0 and Gemini Pro
### Gen AI Statement: Used ChatGPT for general potential function outlines for inputs, outputs, and usage,
### , and for our flowchart ideas. We used Gemini and ChatGPT collectively for general debugging help.





import csv
import unittest
import math



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

    # Jackson's function 

    """
    Calculates average body mass for each penguin species.
    INPUT: data (list of dicts)
    OUTPUT: avg_body_mass (dict {species: avg_mass}) to a new file
    """

    avg_body_mass = {}
    for row in data:
        row_species = row.get("species")
        row_mass = row.get("body_mass_g")
        flipper = row.get("flipper_length_mm")
        if row_mass is None or flipper is None:
            #changed from setting to zero to skipping to avoid skewing
            continue
        
        

        ## Using dict to store mass for each species 

        if row_species not in avg_body_mass:
            avg_body_mass[row_species] = {"total_mass": 0, "count": 0}
        
        avg_body_mass[row_species]["total_mass"] += row_mass
        avg_body_mass[row_species]["count"] += 1 

    
    for species, values in avg_body_mass.items():
        if values["count"] > 0:
            avg_body_mass[species] = values["total_mass"] / values["count"]
        else:
            avg_body_mass[species] = 0
    

   
       

    print(">>> Avg body mass with valid flipper data:", avg_body_mass)
    return avg_body_mass

    


def select_heavy_bills(data):
    # Jackson's function 
    """
    Filters penguins with body mass > 3500g 
    and calculates average bill length.
    INPUT: data (list of dicts)
    OUTPUT: avg_bill_length (float)
    """
    

    # filters penguins above 3500g and a minimum bill depth of 17.0mm
    heavy_bills = [p for p in data 
                   if p.get("body_mass_g") and p["body_mass_g"] > 3500 
                   and p.get("bill_length_mm") and p.get("bill_depth_mm") and p["bill_depth_mm"] >= 17.0]

    if heavy_bills:
        avg_bill_length = sum(p["bill_length_mm"] for p in heavy_bills) / len(heavy_bills)
    else:
        avg_bill_length = 0  # handle no heavy bills


     # with open("average_bill_length_above_3500g.txt", "w") as f:
    #    f.write(f"Average bill length for penguins with body mass > 3500g: {avg_bill_length:.2f} mm\n")


    print(f">>> Avg bill length for body mass > 3500g and above the minimum bill depth of 17.0mm: {avg_bill_length:.3f} mm")
    return avg_bill_length
    
  
  
   


def find_upper_quartile_long_bills(data):
    ### Vittorio's function 
    """
    Identifies penguins in upper 25% of body mass 
    that also have a bill length > 42 mm.
    INPUT: data (list of dicts)
    OUTPUT: num_upper_quartile_long_bills (int)
    """
    


    valid_masses = [p["body_mass_g"] for p in data if p.get("body_mass_g")]
    if not valid_masses:
        return 0

    valid_masses.sort()
    # Use floor to include 75th percentile and above
    index_75 = math.floor(0.75 * len(valid_masses)) - 1
    if index_75 < 0:
        index_75 = 0
    upper_cutoff = valid_masses[index_75]

    long_bills = [
        p for p in data
        if p.get("body_mass_g") and p["body_mass_g"] >= upper_cutoff
        and p.get("bill_length_mm") and p["bill_length_mm"] > 42
    ]

    count = len(long_bills)
    print(f">>> Penguins in top 25% body mass AND bill length > 42mm: {count}")
    return count


def find_heavy_quartile_long_bills(data):
    ### Vittorio's function 
    """
    Counts penguins with body mass > 4000g.
    INPUT: data (list of dicts)
    OUTPUT: count (int)
    """

    # filters based on minimum mass threshold
    heavy_penguins = [p for p in data if p.get("body_mass_g") and p["body_mass_g"] > 4000]

    count = len(heavy_penguins)

    print(f">>> Total penguins with body mass > 4000g: {count}")
    return count



def find_heavy_gentoo_count(data):
    """
    Counts total Gentoo penguins with body mass > 4000g.
    INPUT: data (list of dicts)
    OUTPUT: count (int)
    """

    gentoo_heavy = [p for p in data 
                    if p.get("species") == "Gentoo" 
                    and p.get("body_mass_g") 
                    and p["body_mass_g"] > 4000]

    count = len(gentoo_heavy)

    print(f">>> Total Gentoo penguins with body mass > 4000g: {count}")
    return count

def output_function(data):
    """
    output results of all functions to a new .txt file
    
    """
    with open("penguin_calculation_results.txt", "w") as f:
        f.write("These are the results of the penguin calculations in coding_work.py\n")

        f.write("First Jackson calculated average body mass for each species:\n")
        avg_body_mass = calculate_average_body_mass(data)
        f.write(f"Average Body Mass by Species: {avg_body_mass}\n\n")

        f.write("Next Jackson calculated average bill length for penguins with body mass > 3500g and bill depth >= 17.0mm:\n")
        bill_length = select_heavy_bills(data)
        f.write(f"Average Bill Length for Penguins above 3500g Body Weight and With Bill Depth Greater Than or Equal to 17.0 mm: {bill_length:.2f} mm\n\n")

        f.write("Then Vittorio counted the penguins in the upper 25 percentile of body mass and bill length > 42 mm:\n")
        upper_quartile = find_upper_quartile_long_bills(data)
        f.write(f"Count of Penguins in the Upper 25% of Body Mass With Bill Length > 42 mm: {upper_quartile}\n\n")

        f.write("Next Vittorio counted the total penguins with body mass > 4000g:\n")
        heavy_penguins = find_heavy_quartile_long_bills(data)
        f.write(f"Total Penguins with Body Mass > 4000g: {heavy_penguins}\n\n")

        f.write("Finally Vittorio counted the total Gentoo penguins with body mass > 4000g:\n")
        heavy_gentoos = find_heavy_gentoo_count(data)
        f.write(f"Total Gentoo Penguins with Body Mass > 4000g: {heavy_gentoos}\n")
        f.write("\nPenguins results completed.")
        f.close()



class test_work(unittest.TestCase):
    def test_load_data(self):
        data = load_data("project_work/penguins.csv")
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        self.assertIsInstance(data[0], dict)
        self.assertEqual(set(data[0].keys()), {'', 'species', 'island', 'bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g', 'sex', 'year'})

    def test_calculate_average_body_mass(self):
        data = [
            {"species": "Adelie", "body_mass_g": 3700, "flipper_length_mm": 190},
            {"species": "Adelie", "body_mass_g": 3800, "flipper_length_mm": 195},
            {"species": "Chinstrap", "body_mass_g": 3500, "flipper_length_mm": 200},
            {"species": "Chinstrap", "body_mass_g": None, 'flipper_length_mm': 198},
            {"species": "Gentoo", "body_mass_g": 5000, "flipper_length_mm": 210}
        ]
        data_edge = [
            {"species": "Adelie", "body_mass_g": None, "flipper_length_mm": None},
            {"species": "Chinstrap", "body_mass_g": 100000000000000000, "flipper_length_mm": 200},
            {"species": "Gentoo", "body_mass_g": -5000, "flipper_length_mm": 210}
        ]
        avg_body_mass = calculate_average_body_mass(data)
        self.assertAlmostEqual(avg_body_mass["Adelie"], 3750.0)
        self.assertAlmostEqual(avg_body_mass["Chinstrap"], 3500.0)
        self.assertAlmostEqual(avg_body_mass["Gentoo"], 5000.0)

        avg_mass_edge = calculate_average_body_mass(data_edge)
        self.assertAlmostEqual(avg_mass_edge["Adelie"], 0)
        self.assertAlmostEqual(avg_mass_edge["Chinstrap"], 100000000000000000)
        self.assertAlmostEqual(avg_mass_edge["Gentoo"], -5000)


    def test_select_heavy_bills(self):
        data = [
            {"body_mass_g": 3600, "bill_length_mm": 40, "bill_depth_mm": 18.0},
            {"body_mass_g": 3700, "bill_length_mm": 42, "bill_depth_mm": 17.5},
            {"body_mass_g": 3400, "bill_length_mm": 39, "bill_depth_mm": 16.0},
            {"body_mass_g": None, "bill_length_mm": 41, "bill_depth_mm": 19.0},
        ]

        avg_bill_length = select_heavy_bills(data)

        ## this tests only the first two since the 3rd is below 3500g and the 4th doesn't have mass data 
        self.assertAlmostEqual(avg_bill_length, 41.0)

        data_2 = [
            {"body_mass_g": 4000, "bill_length_mm": 40, "bill_depth_mm": 18.0},
            {"body_mass_g": 4500, "bill_length_mm": 44, "bill_depth_mm": 20.0},
        ]
        avg_bill_length_2 = select_heavy_bills(data_2)
        self.assertAlmostEqual(avg_bill_length_2, 42.0)

        # testing none mass 
        self.assertIsNone({"body_mass_g": None, "bill_length_mm": 41, "bill_depth_mm": 19.0}.get("body_mass_g"))

        
        ## testing edge case, exact mass 3500
        mass_3500 = {"body_mass_g": 3500, "bill_length_mm": 40, "bill_depth_mm": 18.0}
        self.assertAlmostEqual(select_heavy_bills([mass_3500]), 0)  # should not be included
    
    def test_find_upper_quartile_long_bills(self):
        data = [
            {"body_mass_g": 3000, "bill_length_mm": 40},
            {"body_mass_g": 3600, "bill_length_mm": 43},
            {"body_mass_g": 4200, "bill_length_mm": 44},
            {"body_mass_g": 4600, "bill_length_mm": 41},
            {"body_mass_g": 4800, "bill_length_mm": 45}
        ]
        result = find_upper_quartile_long_bills(data)
        self.assertEqual(result, 2)  # top 25% mass + bill length > 42

    def test_find_heavy_quartile_long_bills(self):
        data = [
            {"body_mass_g": 3900},
            {"body_mass_g": 4100},
            {"body_mass_g": 4500},
            {"body_mass_g": None},
        ]
        result = find_heavy_quartile_long_bills(data)
        self.assertEqual(result, 2)  # two above 4000

    def test_find_heavy_gentoo_count(self):
        data = [
            {"species": "Gentoo", "body_mass_g": 4100},
            {"species": "Gentoo", "body_mass_g": 3900},
            {"species": "Adelie", "body_mass_g": 4500},
            {"species": "Gentoo", "body_mass_g": 4200},
        ]
        result = find_heavy_gentoo_count(data)
        self.assertEqual(result, 2)  # only two Gentoo above 4000


        
        

        
        


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
    #for row in csv_data:
    #    print(row)
    

    # for future notice 
    '''
    calculate_average_body_mass(csv_data)
    select_heavy_bills(csv_data)
    find_heavy_gentoo_count(csv_data)
    find_upper_quartile_long_bills(csv_data)
    find_heavy_quartile_long_bills(csv_data)
    '''

    print("These results have been outputted to penguin_calculation_results.txt")
    ## writing to a file
    output_function(csv_data)






if __name__ == "__main__":
    #main()  # optional: runs your main function
    unittest.main()




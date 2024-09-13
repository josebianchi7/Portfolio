# Author: Jose Bianchi
# GitHub username: josebianchi7
# Description: Class named NobelData that reads JSON file containing data on Nobel Prizes and allows search feature.
import os
import json


class NobelData:
    """Represents Nobel Prize data from JSON file"""

    def __init__(self, json_file):
        """Reads JSON file and represents items within file dictionary"""
        
        # Get the current directory of the script
        current_dir = os.path.dirname(__file__)

        # Construct the full path to the input file
        input_file_path = os.path.join(current_dir, json_file)

        # Check if the input file exists
        if not os.path.exists(input_file_path):
            raise FileNotFoundError(f"The file '{json_file}' does not exist in the current directory.")
        
        # Read JSON file and store content to class object
        with open(input_file_path, 'r') as infile:                     
            self._prize_dict = json.load(infile)       


    def get_prize_dict(self):
        """Returns private data member for main JSON dictionary file"""
        return self._prize_dict

    def get_prizes_list(self):
        """Returns list object withing prize dictionary"""
        prizes_dict = self.get_prize_dict()                 # Use 'get' method to retrieve main JSON dictionary

        for prizes_dict_obj in prizes_dict:                 # Iterate over dictionary to retrieve dictionary item
            prizes_list = prizes_dict[prizes_dict_obj]      # Variable name should indicate object type in dictionary

            self._prizes_list = prizes_list
            return self._prizes_list

    def get_prizes_list_dict(self, year, category):
        """Returns dictionary object within prizes list from main dictionary based on year and category"""
        prize_list = self.get_prizes_list()

        for dict_obj in prize_list:
            if year == dict_obj['year'] and category == dict_obj['category']:   # Ensure parameter pair object is found
                self._prizes_list_dict = dict_obj
                return self._prizes_list_dict

    def search_nobel(self, year, category):
        """
        Takes in year and category of Nobel Prize from JSON file, then
        returns sorted list of winner surnames in those parameters.
        """
        dict_obj = self.get_prizes_list_dict(year, category)

        for laureates_obj in dict_obj:
            laureates_list = dict_obj['laureates']

            surnames = sorted(laureates_dict_obj['surname'] for laureates_dict_obj in laureates_list)
            return surnames


if __name__ == '__main__':
    nobel_data = NobelData('nobels.json')
    names = nobel_data.search_nobel("1988", "physics")
    print(names)

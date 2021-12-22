"""
@author: Dibyesh Mishra
@date: 21-12-2021 18:54
"""
import csv
import pathlib

from custom_exception import IndianCensusException


class StateCensusAnalyser:
    """
    desc : working on csv file operations
    """
    num_rows = 0

    def csv_file_data_count(self):
        """
        desc: method to find the total count of records in the csv file
        return: total count of lines in the csv file
        """
        with open("indian_census_data.csv") as my_file:
            for row in my_file:
                self.num_rows += 1
        return self.num_rows

    def check_file_name(self, file_name):
        """
        desc: method to find the name of  the csv file
        return: name of  the csv file
        """
        with open("indian_census_data.csv") as my_file:
            if my_file.name != file_name:
                raise IndianCensusException("not the correct file name")
            else:
                return file_name

    def check_file_extension(self, extension):
        """
       desc: method to return suffix of the csv file
       return: extension
        """
        if pathlib.Path(extension).suffix != ".csv":
            raise IndianCensusException("file format not valid")
        else:
            return extension

    def check_file_delimiter(self, delimiter):
        """
       desc: method to return delimiter used in the csv file
       return: delimiter
        """
        with open("indian_census_data.csv") as my_file:
            sniffer = csv.Sniffer
            my_file = sniffer().sniff(my_file.read())
            delimiter_used = my_file.delimiter
            if delimiter != delimiter_used :
                raise IndianCensusException("wrong delimiter")
            else:
                return delimiter

    def indian_state_file_data_count(self):
        """
        desc: method to find the total count of records in the csv file
        return: total count of lines in the csv file
        """
        with open("indian_state_code_data.csv ") as my_file:
            for row in my_file:
                self.num_rows += 1
        return self.num_rows

    def check_indian_state_file_name(self, file_name):
        """
        desc: method to find the name of  the csv file
        return: name of  the csv file
        """
        with open("indian_state_code_data.csv") as my_file:
            if my_file.name != file_name:
                raise IndianCensusException("not the correct file name")
            else:
                return file_name

    def check_indian_state_file_extension(self, extension):
        """
       desc: method to return suffix of the csv file
       return: extension
        """
        if pathlib.Path(extension).suffix != ".csv":
            raise IndianCensusException("file format not valid")
        else:
            return extension

    def check_indian_state_file_delimiter(self, delimiter):
        """
       desc: method to return delimiter used in the csv file
       return: delimiter
        """
        with open("indian_state_code_data.csv") as my_file:
            sniffer = csv.Sniffer
            my_file = sniffer().sniff(my_file.read())
            delimiter_used = my_file.delimiter
            if delimiter != delimiter_used :
                raise IndianCensusException("wrong delimiter")
            else:
                return delimiter

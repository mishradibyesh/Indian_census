"""
@author: Dibyesh Mishra
@date: 21-12-2021 21:04
"""
import pytest
from custom_exception import  IndianCensusException
from indian_census import StateCensusAnalyser


class TestIndianCensus:

    @pytest.fixture()
    def census(self):
        census = StateCensusAnalyser()
        return census

    def test_number_of_records(self,census):
        assert census.csv_file_data_count() == 30

    def test_file_name_if_invalid(self, census):
        with pytest.raises(IndianCensusException) as exception:
            census.check_file_name("indian_census_data1.csv")
            assert exception.__str__() == "not the correct file name"

    def test_file_extension_if_invalid(self, census):
        with pytest.raises(IndianCensusException) as exception:
            census.check_file_extension("indian_census_data1.txt")
            assert exception.__str__() == "file format not valid"

    def test_file_delimiter_if_invalid(self, census):
        with pytest.raises(IndianCensusException) as exception:
            census.check_file_delimiter(".")
            assert exception.__str__() == "wrong delimiter"

    def test_number_of_records_indian_state_file(self,census):
        assert census.indian_state_file_data_count() == 38

    def test_file_name_indianState_if_invalid(self, census):
        with pytest.raises(IndianCensusException) as exception:
            census.check_indian_state_file_name ("indian_state_code.csv")
            assert exception.__str__() == "not the correct file name"

    def test_indian_state_file_extension_if_invalid(self, census):
        with pytest.raises(IndianCensusException) as exception:
            census.check_indian_state_file_extension ("indian_state_code_data.txt")
            assert exception.__str__() == "file format not valid"

    def test_indian_state_file_delimiter_if_invalid(self, census):
        with pytest.raises(IndianCensusException) as exception:
            census.check_indian_state_file_delimiter(".")
            assert exception.__str__() == "wrong delimiter"
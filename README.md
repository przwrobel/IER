# Introduction to Engineering Research - Data_analysis_code.py

This project contains the raw source code (Data_analysis_code.py) used to analyse the Fitbit dataset: Data_IER.
This code can analyse only the files of an identical structure as "Data_IER.csv".
"Data_analysis_code.py" is used to create "Table One" and for filtering the data in "Data_IER.csv" to group the study participants in following categories: male, female, overall. 
These are further narrowed down by year of participation. Separate dataframes are created in previously mentioned categories.
Dataframes with step count measured with app and omron device are created and averages are calculated for weekdays and weekends.
T-tests are performed with division by: year, gender, week part.
Results are saved to "results.txt" file generated in the same directory in which "Data_analysis_code.py" is placed.

### Data

Data for the analysis is available under this link: https://gitlab.tudelft.nl/yturkyilmaz/Introduction_to_Engineering_Research/-/tree/master/Data_analysis

## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes. 

### Prerequisites

Python v3.7.7 or higher with following libraries: Pandas, TableOne and SciPy
Development environment - preferably Spyder - https://www.spyder-ide.org

### Installing

To perform data analysis:
	- put file "Data_IER.csv" in the same folder as the "Data_analysis_code.py"
	- open "Data_analysis_code.py" with Spyder (or other development environment)
	- Compile and run the code
	- see console for "Table One" in LateX formatting
	- see file "results.txt" for analysis results

## Built With

  - Python - https://www.python.org
  - TableOne - https://pypi.org/project/tableone/
  - SciPy - https://www.scipy.org
  - Pandas - https://pandas.pydata.org

## Versioning

No versioning is implemented for this project.

## Author

  - Przemysław Wróbel
	
## License

This project is licensed under the [CC0 1.0 Universal](LICENSE.md)
Creative Commons License - see the [LICENSE.md](LICENSE.md) file for
details

## Attribution 
Inclusion of Author's name and surname as part of the credits.

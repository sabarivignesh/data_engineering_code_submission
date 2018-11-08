# Test Cases:

## Overview:

ETL Pipeline is tested with three test scenarios to ensure that the data that has been loaded from a source to the destination after business transformation is accurate.

### Data Completeness Validation:
        
        This test is done to check whether all data records from the source system (JSON) is loaded into the target system (PostgreSQL Table).
        
### Data Quality Validation:

        This test is done to check the quality of data loaded in the target system (PostgreSQL table) compared with the source system   (JSON).
        
### Requirement Structure Validation:

        This test is done to validate whether the data in target system (PostgreSQL table) are in-line with the business requirement     document.

## Test cases – Step by Step:

### Test case 1 

#### Source System: 
    JSON File – Earthquakes dataset.

#### Target System:
    PostgreSQL – Earthquakes table.
	
#### Check Condition: 
    Check whether total count of records in source system is matching with the total count of records in target system.

#### Success Case: 
    Total count of records in source system matches with the total count of records in target system.

### Test case 2

#### Source System: 
    JSON File – Earthquakes dataset.
	
#### Target System:
    PostgreSQL – Earthquakes table.

#### Check Condition: 
    Check whether max() value of “size” in source system is matching with max() value of “magnitude” in target system

#### Success Case: 
    max() value of “size” in source system matches with max() value of “magnitude” in target system.

### Test case 3

#### Source System: 
    JSON File – Earthquakes dataset.
	
#### Target System:
    PostgreSQL – Earthquakes table.

#### Check Condition: 
    Check whether the table structure and datatype of columns in target system are in-line with the business requirements.

#### Success Case: 
    Datatype of columns in target system are in-line with the business requirement document.
    Table structure is in-line with the business requirement structure.

## Scope of Test cases:

Current scope of the ETL Testing cases are done from an User acceptance point of view.
	
 




# MSE Seminar Data Base Systems Spring 17 on Triple Stores
This is the repository for the MSE Seminar Data Base Systems Spring 2017 on "Evaluating Open Source Triple Stores with Massive Data from the example of Virtuoso Universal DB Server, Apache Jena TDB and RDFLib/PostgreSQL DB".

## Dataset

For this seminar we use the "Berlin SPARQL Benchmark" (BSBM, v3.1 2011): http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/ with dataset Product.

Queries: For the benchmark we implement the following queries: http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/ExploreUseCase/index.html  

In order to get the data we used the data generation tool: http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/BenchmarkRules/index.html#datagenerator . 

Content see below. Download-Link for all files: https://drive.switch.ch/index.php/s/xvHCPcPkVlKjYzJ. 

|File  	            |Triples    |
|---	            |---	    |
|scale1000.nt   	| 27'886 	|
|scale5000.nt   	| 1'620'320	|
|scale10000.nt   	| 3'421'251	|
|scale30000.nt   	| 10'510'208|

Note: If you like to generate your own data for test use the generate script. 
Switch to the bsbmtools-0.2 directory and generate the sample data. 
Example: ``./generate -fc -pc 10000 -ud -fn scale10000 -s ttl``


## RDFLib/PostgreSQL
To compare your specific triple store system with PostgreSQL we prepared a setup with Postgres and RDFLib.
 
### Setup
  1. Install PostgreSQL 9.6 and create a database called "benchmark"
  2. Install Python 3.6 and pip 3
  3. Clone this repository 
  ``git clone https://github.com/geometalab/MSE-Database-Seminar-Triple-Stores.git``
  4. Get the benchmark data from https://drive.switch.ch/index.php/s/xvHCPcPkVlKjYzJ  
  5. To import the data into postgres us the sql dump files 
  ``psql -U postgres -h localhost benchmark < dump_scale1000.sql``
  6. Install the project requirements with pip3 
  ``pip3 install -r requirements.txt``

Note: With the store_data.py script you are able to import the Triple Store Files (.nt) direct into PostgreSQL. (The recommended way is to use the SQL dump files).
To import the data, run the store_data.py (this could take a while): ``python3 store_data.py``.

### Queries

As you can see in the folder 'rdflib/' of our github repo indicated above, there is a queries.py file with the queries from the benchmark with filled random variables.

Your goal is now to implement the same queries with your specific framework and compare them with the RDFLib/PostgreSQL setup.      

To run the queries on the RDFLib/PostgreSQL setup use the query_data.py script. 
``python3 query_data.py`` The output will look somehow as following:
```
Query: query_1 , Count: 10, Time: 26.906s
Query: query_2 , Count: 14, Time: 0.658s
Query: query_3 , Count: 10, Time: 46.187s
Query: query_4 , Count: 10, Time: 136.501s
Query: query_5 , Count: 5, Time: 24.915s
Query: query_6 , Count: 21467, Time: 98.267s
Query: query_7 , Count: 5, Time: 32.379s
Query: query_8 , Count: 3, Time: 0.120s
Query: query_10 , Count: 0, Time: 32.155s
Query: query_11 , Count: 10, Time: 1.077s
Query: query_12 , Count: 8, Time: 0.044s
```

Notes:
 - RDFLib doesn't support DESCRIBE, so the query number 8 is not possible in RDFLib.
 - RDFLib with SQLAlchemy implemented aka lazy loading, so the query immediately returns and objects are queries after accessing or interating through the result set.


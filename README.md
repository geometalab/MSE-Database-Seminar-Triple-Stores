# MSE Seminar Data Base Systems Spring 17 on Triple Stores
This is the repository for the MSE Seminar Data Base Systems Spring 2017 on "Evaluating Open Source Triple Stores with Massive Data from the example of Virtuoso Universal DB Server, Apache Jena TDB and RDFLib/PostgreSQL DB".


## Postgres with rdflib as reference
To compare your individual triple store system with postgres we prepared a setup with postgres and rdflib.
 
### Setup
  1. Install Postgres 9.6 and create a database called "benchmark"
  2. Install Python 3.6 and pip 3
  3. Clone this repository ``git clone https://github.com/geometalab/MSE-Database-Seminar-Triple-Stores.git``
  4. Get the benchmark data from https://drive.switch.ch/index.php/s/xvHCPcPkVlKjYzJ  
  5. To import the data into postgres us the sql dump files ``psql -U postgres -h localhost benchmark < dump_scale1000.sql``
  6. Install the project requirements with pip3 ``pip3 install -r requirements.txt``
  7. Now you could run the queries ``python3 query_data.py``

### Dataset
Link: https://drive.switch.ch/index.php/s/xvHCPcPkVlKjYzJ

|File  	            |Triples    |
|---	            |---	    |
|scale1000.nt   	| 27'886 	|
|scale5000.nt   	| 1'620'320	|
|scale10000.nt   	| 3'421'251	|
|scale30000.nt   	| 10'510'208|

We used the data generation tool from the Berlin SPARQL Benchmark (BSBM). 
http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/BenchmarkRules/index.html#datagenerator  
  
If you like to generate your own data for test use the generate script. 
Switch to the bsbmtools-0.2 directory and generate the sample data. 
Example: ``./generate -fc -pc 10000 -ud -fn scale10000 -s ttl``

### Queries
For the benchmark we implement the following queries: 
http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/ExploreUseCase/index.html  

As you can see in the folder rdflib there is a queries.py file with the queries from the benchmark with filled random variables.
(rdflib doesn't support DESCRIBE so the query number 8 is not possible)  
Your goal is now to implement the same queries with your specific framework and compare them with the postgres rdflib setup.

### Additional
With the store_data.py script you are able to import the TripleStoreFiles (.nt) direct into postgres. (The recommended way is to us the sql dump files)
To import the data run the store_data.py (this could take awhile) ``python3 store_data.py``

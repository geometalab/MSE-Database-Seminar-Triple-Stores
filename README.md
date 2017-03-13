# MSE Seminar Data Base Systems Spring 17 on Triple Stores
This is the repository for the MSE Seminar Data Base Systems Spring 2017 on "Evaluating Open Source Triple Stores with Massive Data from the example of Virtuoso Universal DB Server, Apache Jena TDB and RDFLib/PostgreSQL DB".


## Postgres with rdflib as reference
To compare your individual triple store system with postgres we prepared a setup with postgres and rdflib.
 
### Setup
  1. Install Postgres 9.6. (I recommend to use the the docker container from https://hub.docker.com/_/postgres/)
  2. Install Python 3.6
  3. Clone this repository ``git clone https://github.com/geometalab/MSE-Database-Seminar-Triple-Stores.git``
  4. Switch to the bsbmtools-0.2 directory and generate the sample data ``./generate -fc -pc 10000 -ud -fn scale10000 -s ttl`` 
  5. Move the scale10000.ttl file into the rdflib directory and edit the config.ini for the setup
  6. To import the data into the postgres database run the store_data.py (this could take awhile) ``python3 store_data.py``
  7. Now you could run the queries ``python3 query_data.py``

## Queries
For the benchmark we implement the following queries:  
http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/ExploreUseCase/index.html  

As you can see in the folder rdflib there is a queries.py file with the queries from the benchmark with filled random variables.  
(rdflib doesn't support DESCRIBE so the query number 8 is not possible)  
Your goal is now to implement the same queries with your specific framework and compare them with the postgres rdflib setup.


## Data generation
For the Benchmark we use the Berlin SPARQL Benchmark (BSBM). (http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/BenchmarkRules/index.html#datagenerator)

This project provides a data generator for RDF data.

### How to generate data with bsbmtools
Switch to the /bsbmtools-0.2 directory and run the generate script.  
And run the command:
```
 ./generate -fc -pc 10000 -ud -fn scale10000 -s ttl
```

The scale10000.ttl file contains now 3421251 triples and is the base for the benchmark.


### Jena example
Build:
```
mvn clean compile assembly:single
```

Run:
```
java -jar target/TripleStoreSeminar-1.0-SNAPSHOT-jar-with-dependencies.jar 
```

# MSE Seminar Data Base Systems Spring 17 on Triple Stores
This is the repository for the MSE Seminar Data Base Systems Spring 2017 on "Evaluating Open Source Triple Stores with Massive Data from the example of Virtuoso Universal DB Server, Apache Jena TDB and RDFLib/PostgreSQL DB".

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


## Jena example
Build:
```
mvn clean compile assembly:single
```

Run:
```
java -jar target/TripleStoreSeminar-1.0-SNAPSHOT-jar-with-dependencies.jar 
```

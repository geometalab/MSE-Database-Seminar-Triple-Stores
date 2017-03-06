# Triple Store Seminar
This is the repository for the MSE Seminar Data Base Systems Spring 2017 on "Evaluating Open Source Triple Stores with Massive Data from the Example of Virtuoso Universal DB Server, Apache Jena TDB and RDFLib/PostgreSQL DB".

## Data generation
For the Benchmark we use the Berlin SPARQL Benchmark (BSBM). (http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/BenchmarkRules/index.html#datagenerator)

This project provides a data generator for RDF data.

### How to generate data
Switch to the /bsbmtools-0.2 directory and run the generate script.

```
$ ./generate -h

Usage:

Possible options are:
	-s <output format>
		where <output format>: nt (N-Triples), trig (TriG), ttl (Turtle), sql (MySQL dump),
			virt (Virtuoso SQL dump), monetdb (SQL), xml (XML dump)
		default: nt
		Note:	By chosing a named graph output format like TriG,
			a named graph model gets generated.
	-pc <product count>
		default: 100
	-fc	Switch on forward chaining which is by default off
	-dir <output directory>
		The output directory for the Test Driver data
		default: td_data
	-fn <dataset file name>
		The file name without the output format suffix
		default: dataset
	-ufn <update dataset file name>
		The file name without the output format suffix
		default: dataset_update
	-nof <number of output files>
		The number of output files. Only for -s nt or ttl
		default: 1
	-ud Switch on generation of update dataset
	-tc <number of update transactions>
		Should be used in combination with -ud.
		default: 1000
	-ppt <number of products per update transactions>
		Should be used in combination with -ud.
		default: 1

```

## Queries
http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/ExploreUseCase/index.html


## Example
Build:
```
mvn clean compile assembly:single
```

Run:
```
java -jar target/TripleStoreSeminar-1.0-SNAPSHOT-jar-with-dependencies.jar 
```

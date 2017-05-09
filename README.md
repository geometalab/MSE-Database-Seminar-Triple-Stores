# MSE Seminar Data Base Systems Spring 17 on Triple Stores
This is the repository for the MSE Seminar Data Base Systems Spring 2017 on "Evaluating Open Source Triple Stores with Massive Data from the example of Virtuoso Universal DB Server, Apache Jena TDB and RDFLib/PostgreSQL DB".

## The Benchmark

For this seminar we use the "Berlin SPARQL Benchmark" (BSBM, v3.1 2011): http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/ with dataset Product.

### Queries

For the benchmark we implement the following queries: http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/ExploreUseCase/index.html  

### Dataset

In order to get the data we used the data generation tool: http://wifo5-03.informatik.uni-mannheim.de/bizer/berlinsparqlbenchmark/spec/BenchmarkRules/index.html#datagenerator . 

Content see below. Download-Link for all files: https://drive.switch.ch/index.php/s/xvHCPcPkVlKjYzJ. 

|File  	            |Triples    |
|---	            |---	    |
|scale1000.nt   	| 27'886 	|
|scale5000.nt   	| 1'620'320	|
|scale10000.nt   	| 3'421'251	|
|scale30000.nt   	| 10'510'208|

Notes: 
 - If you like to generate your own data for test use the generate script. Switch to the bsbmtools-0.2 directory and generate the sample data. Example: ``./generate -fc -pc 10000 -ud -fn scale10000 -s ttl``
 - The SQL dump files have beend created using this PostgreSQL command ``pg_dump --format=c benchmark_db > outfile.sql``. format=c indicated 'custom' which is also compressing and which is the most flexible way to backup PostgreSQL data.

## RDFLib
To have a second technology to compare the SPARQL queries with, we us RDFLib which enables to load a triple store file and allows to do queries on the data.


### Setup
  1. Install Python 3.6 and pip 3
  2. Clone this repository 
  ``git clone https://github.com/geometalab/MSE-Database-Seminar-Triple-Stores.git``
  3. Install the project requirements with pip3 
  ``pip3 install -r requirements.txt``
  4. Get the benchmark data from https://drive.switch.ch/index.php/s/xvHCPcPkVlKjYzJ (The N-Triple (.nt) files are the relevant ones)  
  
### Run the queries
To run the SPARQL queries with the RDFLib library there is the ``in_memory_queries.py`` script in the folder ``pyrdflib``.
It it takes the data file as input parameter (-f file_path). As an example usage consider the following:  

``python in_memory_queries.py -f /path/to/file/scale5000.nt``

The computation will run for a while. The main work is to load and parse the data file. 
The output will look somehow as following:
```
Start parsing
Finished parsing
Parse time: 125.627s
Query: query_1 , Count: 10, Time: 1.107s
Query: query_2 , Count: 16, Time: 0.044s
Query: query_3 , Count: 10, Time: 0.192s
Query: query_4 , Count: 10, Time: 0.268s
Query: query_5 , Count: 5, Time: 0.851s
Query: query_6 , Count: 2950, Time: 0.759s
Query: query_7 , Count: 1, Time: 0.104s
Query: query_8 , Count: 2, Time: 0.031s
Query: query_10 , Count: 1, Time: 0.134s
Query: query_11 , Count: 10, Time: 0.006s
Query: query_12 , Count: 8, Time: 0.017s
```



## PostgreSQL
To include PostgreSQL into the benchmarke we use the relational schema of the data provided by the "Berlin SPARQL Benchmark". 
The generation of this data will look like the following: 
``./generate -fc -pc 1000 -ud -fn scale1000 -s sql``
 
### Setup
  1. Install PostgreSQL 9.6 and create a database called **benchmark**
  2. Clone this repository 
  ``git clone https://github.com/geometalab/MSE-Database-Seminar-Triple-Stores.git``
  3. Get the benchmark data from https://drive.switch.ch/index.php/s/xvHCPcPkVlKjYzJ  
  4. To import the data into PostgreSQL use the SQL **.psql** files 
  ``psql -U postgres -h localhost -p 5432 benchmark < scale1000.psql``
  
### Run the relational queries
To run the relational queries you have to provide a **benchmark** database with the stored data.
All the relational queries are in the **relational_queries.psql** file in the folder **postgres**.
For the execution simply use the following command: 
``psql -U postgres -h localhost -p 5432 < relational_queries.psql``

### pgbench
Postgres provides a tool for benchmarks called **pgbench**, it helps to analyse the postgres performance.
Our relational SQL queries could also be executed with pgbench.
To simplify this porccess we provide the bash script **psql_benchmark.sh**  in the **postgres**  folder.

Example usage:
```
./psql_benchmark.sh USERNAME PASSWORD DATABASE
```

Example output:
```
Query: query_1.sql
------------------------
transaction type: Custom query
scaling factor: 1
query mode: simple
number of clients: 1
number of threads: 1
number of transactions per client: 10
number of transactions actually processed: 10/10
latency average: 38.978 ms
tps = 25.655432 (including connections establishing)
tps = 25.908951 (excluding connections establishing)
```

With the **tps** (transactions per second) value you are able to calculate the time for the queries.
In our example the tps of query_1 is 25.655432, thus the average time is 0.0389 sec.

### PostgresSQL Configuration
To optimise the query and import speed you could set the following settings. (Be aware this settings aren't recommended in a productive system) 
Edit the postgresql.conf file, by default it is located in the /etc/postgresql/9.6/main folder.  
OS X 8GB: 
```
fsync = off
max_connections = 5
shared_buffers = 512MB
effective_cache_size = 2GB
work_mem = 87381kB
maintenance_work_mem = 512MB
min_wal_size = 100MB
max_wal_size = 100MB
checkpoint_completion_target = 0.5
wal_buffers = 16MB
default_statistics_target = 100
```

Windows 16 GB:
```
fsync = off
max_connections = 5
shared_buffers = 512MB
effective_cache_size = 4GB
work_mem = 180588kB
maintenance_work_mem = 1GB
min_wal_size = 100MB
max_wal_size = 100MB
checkpoint_completion_target = 0.5
wal_buffers = 16MB
default_statistics_target = 100
```

The remaining settings could be let on their default values.


## Notes
 - RDFLib doesn't support DESCRIBE, so the query number 9 is not possible in RDFLib.
 - RDFLib with SQLAlchemy implemented aka lazy loading, so the query immediately returns and objects are queries after accessing or interating through the result set.

# Overview
This repository provides an interface to encode substrait structures.

Initially, we want to provide an interface to build the structures directly so that
it's possible to create variations of a substrait message without too much overhead.
The next step would be a higher-level API to build the substrait messages without
having to craft too many details manually.


# Motivation
The point of this repository is partially educational and partially for prototyping
and experimentation.

* Writing this code will help me become familiar with the aspects of the substrait
  protocol and how to execute it with Acero.
  
* I am interested in generating and transforming substrait plans from languages
  other than SQL and benchmarking these operations in an embedded environment.
  
* I want to de-couple my implementation from other, larger projects (such as ibis
  or duckdb). The larger projects haven't generalized their modules (for good
  reason), but generalizing their modules is too difficult for me to bootstrap my
  learning and research from.

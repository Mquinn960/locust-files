# Locust File Repository

This repository contains any demo locust files used within
the Locust Test system.

## Locust Files

### Dummy

- ```/dummy/locustfile.py```

This is the current dummy file used in demo setups. This file
is the default file found in the Locust quick start and is
used to test deployments are functioning correctly.

### Foobar

- ```/foobar/locustfile.py```

A test file conversant with the current Mock Server API
implementation containing 2 routes, ```foo``` and ```bar```
respectively.

- ```/api/v1/foo```
  - GET
  - query: foobar
  - note: contains dummy intermittent failures 
- ```/api/v1/bar```
  - GET

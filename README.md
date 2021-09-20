# digeiztest
# Test Digeiz

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/kapserge/digeiztest.git
$ cd digeiztest
```
Once `pip` has finished downloading the dependencies:
```sh

$ python manage.py runserver
```
the command  add test records to the API:
```sh

$ python manage.py Accounttestdata

```
the command  add test records to the API with bulk :
```sh

$ python manage.py BulkAccountdata


```
the command to make unit tests of the view and the model 
```sh

$ python manage.py test


```

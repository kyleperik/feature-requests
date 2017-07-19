# Feature Requests

[ ![Codeship Status for kyleperik/feature-requests](https://app.codeship.com/projects/c9223550-4efa-0135-7042-16b8375812a9/status?branch=master)](https://app.codeship.com/projects/233879)

Project for recording clients' feature requests for other software

## Technology Stack

**Operating System**
This app was developed using Arch Linux with the Budgie Desktop Environment, but will work perfectly fine on Ubuntu

**Backend**
Server side scripted with Python 3 using flask and SQL Alchemy

**Frontend**
Frontend designed with Vue JS

## Running

### Installation

To install, simply change directory to project root, then `pip install ./`

### Configuration

Configuring is fairly easy, first create `config.py` in the project root.

```ini
SECRET_KEY=<key here>
```

Then create a environment variable `FEAT_REQS_SETTINGS` with the path to your configuration file:

`~/path/to/project/config.py`

Finally, run `python start.py` in the project root, and you should be good to go.

## Running tests

Make sure you have `pytest` installed, then run `pytest` in the project root to run all tests

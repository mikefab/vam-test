# vam-form-fetcher

This repo fetches and stores responses to forms from the [ONA platform](https://api.ona.io/static/docs/index.html)

#### Install & Run
    $ docker run --name my-mongo -d -v /tmp/mongodb:/data/db -p 27017:27017 mikefab/mongodb
    $ make initialize-db # Runs MongoDB as docker image, and creates a db if one doesn't already exist
    $ python3 main.py    # Fetches and saves form responses

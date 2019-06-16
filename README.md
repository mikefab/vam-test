# vam-form-fetcher

An application to fetch and store responses to forms from the [ONA platform](https://api.ona.io/static/docs/index.html)

#### Install
    $ docker run --name my-mongo -d -v /tmp/mongodb:/data/db -p 27017:27017 mikefab/mongodb
    $ make initialize-db
    $ python main.py

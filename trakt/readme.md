## How to get data?

Trakt.tv API sucks!!

To export your data follow these steps:
- Create an [Trakt.tv application](https://trakt.tv/oauth/applications) to get your own `client_id` and `client_secret`
    - Fill the name and description of the application(any name you like)
    - In Redirect uri write `urn:ietf:wg:oauth:2.0:oob`, leave the rest empty and click on SAVE APP.
- Run [this](https://github.com/xbgmsharp/trakt/) script and it will generate `config.ini`.
- Open that config file and paste your `client_id` and `client_secret`.
- Then just run `python export_trakt.py` to export movie data
    - `python export_trakt.py -t shows` to export TV show data

- Using this(https://github.com/glensc/python-pytrakt) trakt package

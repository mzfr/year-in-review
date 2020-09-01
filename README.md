# chess data Analysis

This repository contains the code and data for the analysis that I did on all the chess games that I have played till now.

## How to download the data?

* __Lichess.org data__

You can either download it from the lichess website by clicking the `download` button present on your profile page.

If you want to download it using curl then run the following command:

```
curl https://lichess.org/games/export/<YOUR_USERNAME_HERE> > lichess.pgn
```

* __Chess.com data__

So there is no GUI method for this. You can try to download the data from the terminal by running the following command:

```
for g in $(curl -Ls https://api.chess.com/pub/player/<YOUR_USERNAME_HERE>/games/archives | jq -rc ".archives[]") ; do curl -Ls "$g" | jq -rc ".games[].pgn" ; done >> chess.com.pgn
```

But there is an issue with this method. The PGN which is downloaded couldn't be parsed properly by `python-chess` library.

* **Recommended method**

    For this purpose I have written a python script to download the data and make a pgn file. Use [chesscom_downloader.py](./chesscom_downloader.py) file to download the data. Make sure to change the username in the file.


***

Once you have downloaded the data use the code present in the Jupyter notebook to generate the graph and have a properly analysis.

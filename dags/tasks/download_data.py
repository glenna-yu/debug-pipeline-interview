import shutil
import urllib.request as request

from contextlib import closing

# data from ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/


def download_data():
    stations_url = "ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt"
    with closing(request.urlopen(stations_url)) as r:
        with open("/root/data/ghcnd-stations.txt", "wb+") as f:
            shutil.copyfileobj(r, f)

    stations_url = "ftp://ftp.ncdc.noaa.gov/pub/data/ghcn/daily/ghcnd-states.txt"
    with closing(request.urlopen(stations_url)) as r:
        with open("/root/data/ghcnd-states.txt", "wb+") as f:
            shutil.copyfileobj(r, f)

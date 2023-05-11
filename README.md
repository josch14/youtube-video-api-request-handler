# Youtube Video API: Video Request Handler in Python
Collect information about a Youtube video via YouTube Data API in Python.
The code serves as a minimal example and can be extended to get information
for multiple videos with a single API request, to save received information to
local files (e.g. CSV file), or to request only a subset of fields (e.g. the 
video category).

See [here](https://developers.google.com/youtube/v3/getting-started) for 
information about the YouTube Data API and how to use it (including available 
resources, fields and parameters), and how authorization credentials can be
obtained.

- [Youtube Video Categories](https://gist.github.com/dgp/1b24bf2961521bd75d6c)

## Setup
Install Google API Client.

```
pip install --upgrade google-api-python-client
```

In order to make requests to the Youtube Video API, you need your personal 
API key (authorization credentials) (e.g. `'AIzaSyD9UI3EtVM0O_CwYsZ7k8EhCBmxmLdriG4'`).
You can pass the key with every request via command line, or change the default
value of the corresponding argument within `request_info.py`.

## Example
Pass the id of the desired video (e.g. `0EqSXDwTq6U` for `https://www.youtube.com/watch?v=0EqSXDwTq6U`) and your API key via command line. The command 

```
python request_info.py -k 'AIzaSyD9UI3EtVM0O_CwYsZ7k8EhCBmxmLdriG4' -id 0EqSXDwTq6U
```

results in the response

```
{
    "kind": "youtube#video",
    "etag": "jjcEc6gzCy35w7VOHXgfJCURXEA",
    "id": "0EqSXDwTq6U",
    "snippet": {
        "publishedAt": "2010-08-24T15:53:42Z",
        "channelId": "UCVc1qz2PalWA-ZCsnTWSioQ",
        "title": "Charlie bit my finger! ORIGINAL",
        "description": "Charlie getting bitten by he's tiny winy little brother this shall make you AWWWWW! comment oxo.",
        "thumbnails": {
            "default": {
                "url": "https://i.ytimg.com/vi/0EqSXDwTq6U/default.jpg",
                "width": 120,
                "height": 90
            },
            "medium": {
                "url": "https://i.ytimg.com/vi/0EqSXDwTq6U/mqdefault.jpg",
                "width": 320,
                "height": 180
            },
            "high": {
                "url": "https://i.ytimg.com/vi/0EqSXDwTq6U/hqdefault.jpg",
                "width": 480,
                "height": 360
            }
        },
        "channelTitle": "jasminmakeup",
        "tags": [
            "charlie",
            "bit",
            "me",
            "funnybabies"
        ],
        "categoryId": "23",
        "liveBroadcastContent": "none",
        "localized": {
            "title": "Charlie bit my finger! ORIGINAL",
            "description": "Charlie getting bitten by he's tiny winy little brother this shall make you AWWWWW! comment oxo."
        }
    }
}
```

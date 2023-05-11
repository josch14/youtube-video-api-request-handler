import json
import googleapiclient.discovery
import argparse


API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
 
parser = argparse.ArgumentParser()
parser.add_argument('-id', '--video_id', type=str, default='0EqSXDwTq6U',
                    help='ID of the Youtube video for which information should be gathered.')
parser.add_argument('-k', '--key', type=str, default="TODO",
                    help='Youtube API key (authorization credentials).')
args = parser.parse_args()


def main(developer_key: str, video_id: str):

    # API resource
    yt_api = googleapiclient.discovery.build(
            API_SERVICE_NAME, 
            API_VERSION, 
            developerKey=developer_key 
    )

    # information for up to 50 videos can be obtained with a single request
    # if desired, extend this list with further video IDs 
    video_ids = [video_id]

    # when interested in only a specific field (e.g. the video category), 
    # you may use the corresponding attribute or just filter the response 
    # for the desired attribute
    request = yt_api.videos().list(
        part='id,snippet',
        id=video_ids,
        # fields='items(id, snippet(categoryId))'
    )

    # send request and receive response
    try:
        response = request.execute()
    except Exception as e:
        print('Request failed: ' + str(e))
        exit()

    # print info for videos with successful request
    video_ids_success = []
    for video_info in response['items']:
        print(json.dumps(video_info, indent=4))
        video_ids_success.append(video_info['id'])
    
    for id in video_ids:
        if id not in video_ids_success:
            print(f'No information received for video with id \'{video_id}\'. '
                  'Check video id or whether the video is (still) public.')
        

if __name__ == "__main__":
    developer_key = args.key
    video_id = args.video_id

    if developer_key == "TODO":
        print('Please specify your Youtube API key by passing it via the '
              '--developer_key argument or change its default value within request_info.py.')
        print('Get your authorization credentials / API key '
              '@ https://developers.google.com/youtube/registering_an_application.')
        exit()

    main(developer_key, video_id)

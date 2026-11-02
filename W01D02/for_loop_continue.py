video_stream = ['introduction', 'advertisement',
                'advertisement', 'main agenda',
                'topic discussion', 'advertisement',
                'conclusion', 'advertisement']

for video in video_stream:
    if video == 'advertisement':
        continue  # skip rest of the lines and move to next item
    print(f"Watching {video}")
    print('This video is amazing!!', len(video))

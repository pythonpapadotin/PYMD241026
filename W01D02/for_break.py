video_stream = ['introduction', 'advertisement',
                'advertisement', 'main agenda',
                'topic discussion', 'advertisement',
                'conclusion', 'advertisement']

for video in video_stream:
    if video == 'advertisement':
        break  # come out of the for loop, don't watch anything else
    print(f"Watching {video}")
    print('This video is amazing!!', len(video))

print('Out of for loop, line 12')

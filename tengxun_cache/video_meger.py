
import os



video_info = {}

with open('.m3u8', 'r', encoding='utf8') as f:
    lines = f.readlines()
    video_info = {d.strip():None for d in lines if not d.startswith('#')}
    print(video_info)

    sort_video_name = sorted(list(video_info.keys()), key=lambda x:int(x.split('.')[0]))
    print(sort_video_name)

    for k in video_info.keys():
        print(k)

dir_list = os.listdir('.')
print(dir_list)
for dir_name in dir_list:
    if os.path.isdir(dir_name):
        video_name = os.listdir(dir_name)
        print(dir_name, video_name)
        for name in video_name:
            if name in video_info:
                video_info[name] = os.path.join(dir_name, name)

print(video_info)


with open('video_all.ts', 'ab') as v_all:
    for video_name in sort_video_name:
        video_path = video_info[video_name]
        if video_path:
            with open(video_info[video_name], 'rb') as f:
                v_all.write(f.read())
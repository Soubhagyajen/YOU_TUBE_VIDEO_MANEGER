import json

def load_data():
    try:
        with open('youtube.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open('youtube.txt','w') as file:
        json.dump(videos,file)    


def list_all_videos(videos):
    print("\n")
    print("*" *70)
    for index , video in enumerate(videos,start=1):
        print(f"{index}. {video['name']},  duration:{video['time']}")
    print("\n")
    print("*" *70)    

def add_youtube_videos(videos):
    name=input("enter video name")
    time=input("enter video time")
    videos.append({'name':name,'time':time})
    save_data_helper(videos)


def update_youtube_video(videos):
    # list_all_videos(videos)
    # index = int(input("Enter the video number to update"))
    # if 1 <= index <= len(videos):
    #     name = input("Enter the new video name")
    #     time = input("Enter the new video time")
    #     videos[index-1] = {'name':name, 'time': time}
    #     save_data_helper(videos)
    # else:
    #     print("Invalid index selected")
    list_all_videos(videos)
    index = int(input("enter the index number to update videos"))
    if 1<= index <= len(videos):
        name=input("enter the video name:")
        time=input("enter the video duration")
        videos[index-1]={'name':name,'time':time}
        save_data_helper(videos)
    else:
        print("invlaid choice!!!")    

        
def delete_youtube_video(videos):
    list_all_videos(videos)
    indexs = int(input("enter the index to delete the videos:"))
    if 1<= indexs <= len(videos):
        del videos[indexs-1]
        save_data_helper(videos)
    else:
        print("invalid choice")    


def main():
    videos= load_data()
    while True:
        print("\n Youtube Manager | choose an option")
        print("1. list all videos")
        print("2. add youtube videos")
        print("3. update a youtube video details ")
        print("4. delete a youtube video")
        print("5. Exit the app")
        choice =input("enter your choice :")
        print(videos) 
         
        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_youtube_videos(videos)
            case "3":
                update_youtube_video(videos)
            case "4":
                delete_youtube_video(videos)
            case "5":
                break
            case _:
                print("invalid choice!!!") 


if __name__ == "__main__":
    main()                            
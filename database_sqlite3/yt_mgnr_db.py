import sqlite3

conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video(video_id, newname, newtime):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (newname, newtime, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()

def main():
    while True:
        print("\nYoutube manager app with DB")
        print("1. List videos")
        print("2. Add videos")
        print("3. Update videos")
        print("4. Delete videos")
        print("5. Exit app")
        choice = input("Enter a number: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = int(input("Enter video id to update: "))
            newname = input("Enter the video name: ")
            newtime = input("Enter the video time: ")
            update_video(video_id, newname, newtime)
        elif choice == '4':
            video_id = int(input("Enter video id to delete: "))
            delete_video(video_id)
        elif choice == '5':
            cursor.close()
            conn.close()
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()

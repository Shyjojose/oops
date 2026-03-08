# Q) Given a nested folder structure represented as a dictionary, 
# write a recursive function to count the total number of files in the entire
# folder structure.


folder = {
    "files": ["notes.txt", "photo.jpg"],
    "subfolders": [
        {
            "files": ["report.pdf"],
            "subfolders": []
        },
        {
            "files": ["music.mp3", "video.mp4"],
            "subfolders": [
                {
                    "files": ["data.csv"],
                    "subfolders": []
                }
            ]
        }
    ]
}

def count_files(folder):
    # Base case: if there are no subfolders, return the number of files in the current folder
    if not folder["subfolders"]:
        return len(folder["files"])
    
    # Recursive case: count files in the current folder and add the counts from subfolders
    total_files = len(folder["files"])
    for subfolder in folder["subfolders"]:
        total_files += count_files(subfolder)
    
    return total_files

print(count_files(folder))
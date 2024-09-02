from file_manager import list_files, create_file, delete_file
from social_media import initialize_twitter_api, post_tweet
from app_manager import open_application

def main():
    print("Welcome to your AI assistant. How can I assist you today?")
    
    while True:
        command = input("Enter command: ").lower()
        
        if "list files" in command:
            directory = input("Enter directory: ")
            print(list_files(directory))
        
        elif "create file" in command:
            file_name = input("Enter file name: ")
            content = input("Enter content: ")
            print(create_file(file_name, content))
        
        elif "delete file" in command:
            file_name = input("Enter file name: ")
            print(delete_file(file_name))
        
        elif "post tweet" in command:
            api = initialize_twitter_api("API_KEY", "API_KEY_SECRET", "ACCESS_TOKEN", "ACCESS_TOKEN_SECRET")
            message = input("Enter tweet message: ")
            print(post_tweet(api, message))
        
        elif "open app" in command:
            path = input("Enter application path: ")
            print(open_application(path))
        
        elif "exit" in command:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()

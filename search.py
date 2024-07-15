import os
import re

def extract_usernames_from_html(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

   
    usernames = set(re.findall(r'<a[^>]*>(.*?)<\/a>', html_content))
    
    return usernames

def compare_html_files(html_file1, html_file2):
    usernames1 = extract_usernames_from_html(html_file1)
    usernames2 = extract_usernames_from_html(html_file2)

    unique_usernames = usernames2.difference(usernames1)

    return unique_usernames

def write_usernames_to_txt(usernames, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for username in usernames:
            file.write(username + '\n')

if __name__ == "__main__":
    # Input HTML file paths
    html_file1 = input("Enter the path of the followers HTML file: ").strip('"')
    html_file2 = input("Enter the path of the following HTML file: ").strip('"')

    # Output file path
    output_folder = os.path.dirname(html_file2)
    output_file = os.path.join(output_folder, 'unique_usernames.txt')

    unique_usernames = compare_html_files(html_file1, html_file2)
    write_usernames_to_txt(unique_usernames, output_file)

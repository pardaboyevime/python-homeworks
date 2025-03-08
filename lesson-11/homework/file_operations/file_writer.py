def write_file(file_path,content):
    try:
        with open(file_path,'w') as file:
            file.write(content)
        return f'on path {file_path} {content} is writen'
    except Exception as e:
        return e

print(write_file('output.txt','hello world'))

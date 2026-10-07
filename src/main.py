import sys

# Lecture du fichier fpp
file = open('../dist/test.fpp')
file_content = file.read()

def main() -> None:
    global file
    global file_content
    
    print(str(file_content))

main()
file.close()

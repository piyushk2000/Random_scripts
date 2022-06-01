import os

curruntPath='C:/Users/piyus/Desktop/[CN] Data Structures & Algo with Python'

os.chdir(curruntPath)

# Am I in the correct directory?
# print(os.getcwd())

# print(dir(os))

# Print all the current file names

for folder in os.listdir():
        try:
                path = curruntPath + '/'+ folder
                os.chdir (path)
                # print(os.getcwd())

        #     print(folder)

                for f in os.listdir():
                        # print(f)
                # If.DS_Store file is created, ignore it
                        if f == '.DS_Store':
                                continue

                        file_name, file_ext= os.path.splitext(f)
                        # print(file_name)
                        pass

                        # if file_ext == '.mp4':
                        # One way to do this
                        f_number , f_title= file_name.split('.')


                        f_number = f_number.zfill(3)
        #                         # print('{}{}{}'.format(f_number, f_title, file_ext))


                        new_name = '{}{}{}'.format(f_number, f_title, file_ext)

                        # print (new_name)

                        os.rename(f, new_name)

        except:
                pass
import datetime
import os


def organise():
    downloads_path = "D:\\pobrane\\"
    correct_directory = "D:\\wykłady nagrywanie\\sem 6\\"
    changed = []
    with os.scandir(downloads_path) as directory:

        for data in directory:
            if data.is_file() and data.name.endswith(".mp4"):
                # cutting useless name end
                index = data.name.find("-Meet")

                # cutting file format
                if max(0, index):
                    new_name = data.name[:index]
                else:
                    new_name = data.name[:-4]
                # checking prefix of file and creating subdirectory path
                if new_name.startswith('SAD'):
                    sub_dir = "sad\\" + new_name + ".mp4"
                elif new_name.startswith('BIU'):
                    sub_dir = "biu\\" + new_name + ".mp4"
                elif new_name.startswith('SWB'):
                    sub_dir = "swb\\" + new_name + ".mp4"
                    print(sub_dir)
                elif new_name.startswith('ZPR'):
                    sub_dir = "zpr\\" + new_name + ".mp4"
                elif new_name.startswith('Python'):
                    sub_dir = "python\\" + new_name + ".mp4"
                elif new_name.startswith('SBD'):
                    sub_dir = "sbd\\" + new_name + ".mp4"
                # files that are not declared to edit are omitted
                else:
                    continue

                os.rename(r'' + downloads_path + data.name,
                          r'' + correct_directory + sub_dir)
                # creating logfile list for safety with new path
                changed.append(correct_directory + sub_dir)

    stamp = datetime.datetime.now()

    with open("changeLog.txt", 'a') as file:
        file.write("Data log:  {} changed {} items.\n".format(stamp, len(changed)))
        for _ in changed:
            file.write(_ + "\n")


if __name__ == "__main__":
    organise()

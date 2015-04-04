import os


def mkdirp(*directories):
    """Recursively create all directories as necessary"""
    try:
        """ Get the arguments and convert them into list """
        lis = list(directories)

        """ Join the list elements using '/' so that the resulting,
         string is of form, "C:/some/directory/name"
         """
        a = "/".join(lis)
        print(a)

        """ Pythons inbuilt function to create the directories recursively """
        os.makedirs(a)

        """ Check for error while creating directories """
    except OSError as e:
        if e.errno != 17:   # Error number 17 => File exists
            raise
        else:
            pass


print(mkdirp("G:/some", "random", "dir", "tobe", "created"))

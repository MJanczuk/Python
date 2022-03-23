
def S1(Path):
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(Path) if isfile(join(Path, f))]
    return onlyfiles

def S2(Path):
    from os import walk
    filenames = next(walk(Path), (None, None, []))[2]  # [] if no file
    return filenames

def S3(Path):
    import glob
    return(glob.glob(Path+'/*.rec'))

#Test
#mypath = './Dane surowe'
#print(S1(mypath))
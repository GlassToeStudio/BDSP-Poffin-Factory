import difflib
import random
import time
from multiprocessing import Process, Queue


def f2(wordlist, mainwordlist, q):
    for mainword in mainwordlist:
        matches = difflib.get_close_matches(mainword, wordlist, len(wordlist), 0.7)
        q.put(matches)


if __name__ == '__main__':

    # constants (for 50 input words, find closest match in list of 100 000 comparison words)
    q = Queue()
    wordlist = ["".join([random.choice([letter for letter in "abcdefghijklmnopqersty"]) for lengthofword in range(5)]) for nrofwords in range(100000)]
    mainword = "hello"
    mainwordlist = [mainword for _ in range(50)]

    # normal approach
    t = time.time()
    for mainword in mainwordlist:
        matches = difflib.get_close_matches(mainword, wordlist, len(wordlist), 0.7)
        q.put(matches)
    print(time.time()-t)

    # split work into 5 or 10 processes
    processes = 5

    def splitlist(inlist, chunksize):
        return [inlist[x:x+chunksize] for x in range(0, len(inlist), chunksize)]
    print(len(mainwordlist)/processes)
    mainwordlistsplitted = splitlist(mainwordlist, int(len(mainwordlist)/processes))
    print("list ready")

    t = time.time()
    for submainwordlist in mainwordlistsplitted:
        print("sub")
        p = Process(target=f2, args=(wordlist, submainwordlist, q,))
        p.Daemon = True
        p.start()
    for submainwordlist in mainwordlistsplitted:
        p.join()
    print(time.time()-t)
    if q:
        print(q.get())

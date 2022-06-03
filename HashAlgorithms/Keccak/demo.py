import keccak

if __name__ == "__main__":
    s = "37a636d7dafdf259b7287eddca2f58099e98619d2f99bdb8969d7b14498102cc065201c8be9"
    myKeccak = keccak.Keccak()
    myKeccak.keccak((len(s) * 4, s), 1088, 512, 1600, True)

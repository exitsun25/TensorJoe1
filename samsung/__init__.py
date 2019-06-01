from samsung.miner import Samsung

if __name__ == '__main__':
    f = Samsung.read_file()
    extracted = Samsung.extract_kor(f)
    Samsung.change_token(extracted)
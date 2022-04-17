from src import run


while True:
    try:
        code = input("calc> ")
        res = run(code)
        print(res)
    except KeyboardInterrupt:
        break

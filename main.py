from src import run


while True:
    try:
        code = input("calc> ")
        run(code)
    except KeyboardInterrupt:
        break

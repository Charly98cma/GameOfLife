import gameoflife as GoL

def main():
    print("""Welcome to my...

     ██████   █████  ███    ███ ███████      ██████  ███████     ██      ██ ███████ ███████
     ██       ██   ██ ████  ████ ██          ██    ██ ██          ██      ██ ██      ██
      ██   ███ ███████ ██ ████ ██ █████       ██    ██ █████       ██      ██ █████   █████
       ██    ██ ██   ██ ██  ██  ██ ██          ██    ██ ██          ██      ██ ██      ██
         ██████  ██   ██ ██      ██ ███████      ██████  ██          ███████ ██ ██      ███████
    """)
    # Try-except in case the user press Ctr-C
    try:
        while True:
            try:
                dims = int(input("Enter the dimensions (a number) of the world: "))
                break
            except ValueError:
                pass
        GoL.GameOfLife(dims)
    except KeyboardInterrupt:
        pass
    exit(0)

if __name__ == "__main__":
    main()

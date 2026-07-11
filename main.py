from src.loader import load_responses


def main():
    df = load_responses()

    print(df)


if __name__ == "__main__":
    main()
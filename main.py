from src.evaluator import evaluate_dataframe
from src.loader import load_responses
from src.report import print_summary, save_csv_report
from src.statistics import calculate_statistics


def main():
    try:
        print("Loading AI responses...")
        df = load_responses()

        print("Evaluating responses...")
        evaluated_df = evaluate_dataframe(df)

        print("Calculating statistics...")
        statistics = calculate_statistics(evaluated_df)

        print("Saving report...")
        output_path = save_csv_report(evaluated_df)

        print(evaluated_df)
        print_summary(statistics, output_path)

        print("\nEvaluation completed successfully.")

    except (FileNotFoundError, ValueError, KeyError) as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()
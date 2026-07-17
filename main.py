import logging

from src.evaluator import evaluate_dataframe
from src.loader import load_responses
from src.report import print_summary, save_csv_report
from src.statistics import calculate_statistics


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger(__name__)


def main() -> None:
    """Run the complete AI response evaluation pipeline.

    The application performs the following steps:

    1. Load prompt-response pairs from the JSON dataset.
    2. Evaluate each response using the configured quality criteria.
    3. Calculate summary statistics.
    4. Save the evaluation results as a CSV report.
    5. Print the evaluation summary.

    Any file or data validation errors are logged and reported.
    """
    try:
        logger.info("Loading AI responses")
        df = load_responses()

        logger.info("Evaluating responses")
        evaluated_df = evaluate_dataframe(df)

        logger.info("Calculating statistics")
        statistics = calculate_statistics(evaluated_df)

        logger.info("Saving report")
        output_path = save_csv_report(evaluated_df)

        print(evaluated_df)
        print_summary(statistics, output_path)

        logger.info("Evaluation completed successfully")

    except (FileNotFoundError, ValueError, KeyError):
        logger.exception("Evaluation failed")


if __name__ == "__main__":
    main()
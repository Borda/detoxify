import argparse
import json

import pandas as pd
from detoxify.bias_metrics import (
    LANGS,
    MODEL_NAME,
    TOXICITY_COLUMN,
    compute_lang_metrics_for_model,
    convert_dataframe_to_bool,
)


def main():
    with open(TEST) as f:
        results = json.load(f)

    test_private_path = "jigsaw_data/jigsaw-multilingual-toxic-comment-classification/updated_test.csv"
    test_private = pd.read_csv(test_private_path)
    test_private = convert_dataframe_to_bool(test_private)

    test_private[MODEL_NAME] = [s[0] for s in results["scores"]]

    lang_metrics_df = compute_lang_metrics_for_model(test_private, LANGS, MODEL_NAME, TOXICITY_COLUMN)
    print(lang_metrics_df)
    lang_metrics_df.to_csv(TEST[:-9] + "_lang_breakdown.csv")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--res_path", type=str, help="path to the saved results file")
    args = parser.parse_args()
    TEST = args.res_path

    main()

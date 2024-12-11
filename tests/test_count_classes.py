import pytest
import pandas as pd
import numpy as np
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.count_classes import count_classes

# Set seed for reproducibility
np.random.seed(2024)

# Test input data
two_classes_2_obs = pd.DataFrame(
    {
        "class_labels": ["class1", "class2", "class1", "class2"],
        "values": np.round(np.random.uniform(size=4), 1),
    }
)

two_classes_2_and_1_obs = pd.DataFrame(
    {
        "class_labels": ["class1", "class1", "class2"],
        "values": np.round(np.random.uniform(size=3), 1),
    }
)

one_class_2_obs = pd.DataFrame(
    {
        "class_labels": ["class1", "class1"],
        "values": np.round(np.random.uniform(size=2), 1),
    }
)

three_classes_2_obs = pd.DataFrame(
    {
        "class_labels": ["class1", "class2", "class1", "class2", "class3", "class3"],
        "values": np.round(np.random.uniform(size=6), 1),
    }
)

empty_df = pd.DataFrame({"class_labels": [], "values": []})

class_labels = (["class1", "class2", "class1", "class2"],)
class_values = [0.4, 0.7, 0.0, 0.6]

# Expected test outputs
two_classes_2_obs_output = pd.DataFrame(
    {"class": ["class1", "class2"], "count": [2, 2]}
)

two_classes_2_and_1_obs_output = pd.DataFrame(
    {"class": ["class1", "class2"], "count": [2, 1]}
)

one_class_2_obs_output = pd.DataFrame({"class": ["class1"], "count": [2]})

three_classes_2_obs_output = pd.DataFrame(
    {"class": ["class1", "class2", "class3"], "count": [2, 2, 2]}
)

# `count_classes` should return a data frame, or tibble,
# with the number of rows corresponding to the number of unique classes
# in the `class_col` from the original data frame. The new data frame
# will have a `class column` whose values are the unique classes,
# and a `count` column, whose values will be the number of observations
# for each  class
def test_count_classes_succes():
  assert isinstance(count_classes(two_classes_2_obs, "class_labels"), pd.DataFrame)
  assert count_classes(two_classes_2_obs, "class_labels").equals(two_classes_2_obs_output)
  assert count_classes(two_classes_2_and_1_obs, "class_labels").equals(two_classes_2_and_1_obs_output)
  assert count_classes(three_classes_2_obs, "class_labels").equals(three_classes_2_obs_output)


# `count_classes` should return an empty data frame, or tibble,
# if the input to the function is an empty data frame
# and return one row if there is only one class.
def test_count_classes_edge():
  assert count_classes(one_class_2_obs, "class_labels").equals(one_class_2_obs_output)
  assert count_classes(empty_df, "class_labels").empty

# `count_classes` should throw an error when incorrect types
# are passed to the data frame argument
def test_count_classes_errors():
  with pytest.raises(AttributeError):
    count_classes(class_values, class_labels)
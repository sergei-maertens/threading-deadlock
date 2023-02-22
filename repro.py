#!/usr/bin/env python
#
# By itself, this script runs fine. However, combined with coverage.py, it deadlocks:
#
#   COVERAGE_DEBUG=process,pid coverage run repro.py
#

from hypothesis import strategies as st


json_primitives = st.one_of(
    st.none(),
    st.booleans(),
    st.integers(),
    st.floats(allow_infinity=False, allow_nan=False),
    st.text(),
)

def json_collections(values) -> st.SearchStrategy:
    return st.one_of(
        st.dictionaries(keys=st.text(), values=values),
        st.lists(values),
    )


# calling st.recursive at import time is sufficient
st.recursive(json_primitives, json_collections, max_leaves=15)


def main():
    print("irrelevant")


if __name__ == "__main__":
    main()

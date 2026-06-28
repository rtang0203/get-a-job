import copy
import sys
import os

# Add scripts dir to path so we can import build_resume
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))


def test_content_not_mutated():
    """CONTENT module global must not be mutated after a merge."""
    # We can't import build_resume directly (needs reportlab),
    # so test deep_merge in isolation
    from build_resume import deep_merge

    base = {"name": "Test", "skills": {"a": 1, "b": 2}, "items": [1, 2]}
    original = copy.deepcopy(base)
    override = {"skills": {"b": 99, "c": 3}, "items": [3]}

    result = deep_merge(base, override)

    # Base must be unchanged
    assert base == original, f"base was mutated: {base}"
    # Result should have merged values
    assert result["skills"] == {"a": 1, "b": 99, "c": 3}
    assert result["items"] == [3]  # Lists replaced wholesale
    assert result["name"] == "Test"


def test_nested_dicts_merge_recursively():
    """Nested dicts should be recursively merged, not replaced."""
    from build_resume import deep_merge

    base = {"outer": {"inner1": "a", "inner2": "b"}}
    override = {"outer": {"inner2": "B", "inner3": "c"}}

    result = deep_merge(base, override)
    assert result == {"outer": {"inner1": "a", "inner2": "B", "inner3": "c"}}


if __name__ == "__main__":
    test_content_not_mutated()
    test_nested_dicts_merge_recursively()
    print("All tests passed")

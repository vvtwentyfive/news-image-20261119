"""Deliver the day's front page to the grading sandbox.

The finished newspaper image already lives next to this script. This
program's whole job is to place an exact duplicate of it where the
grader expects to find the submission, creating that folder when it
is missing. Nothing is drawn, resized, or re-encoded here: the bytes
travel untouched from the repository into the output folder.
"""

from pathlib import Path


# The image we ship, sitting beside this script in the repository.
SHIP_NAME = "entry.png"

# Where the grader looks for the finished artefact.
GRADER_FOLDER = Path("/output")


def _repository_root() -> Path:
    """Folder holding this script (and therefore the shipped image)."""
    return Path(__file__).resolve().parent


def deliver_front_page() -> Path:
    """Copy the shipped image into the grader's folder, verbatim.

    Returns the path of the copy that was written.
    """
    source = _repository_root() / SHIP_NAME
    target = GRADER_FOLDER / SHIP_NAME
    GRADER_FOLDER.mkdir(parents=True, exist_ok=True)
    target.write_bytes(source.read_bytes())
    return target


deliver_front_page()

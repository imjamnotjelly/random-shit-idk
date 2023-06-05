import sys
from typing import List
from time import sleep


def delay_out(*text: List[str], **kwargs):
    text = " ".join(text)
    # kwargs = {end: str, delaySeconds: float, duration: float, cursor: bool}
    end = kwargs.get("end") or "\n"
    delaySeconds = kwargs.get("delaySeconds") or .15
    if "duration" in kwargs:
        delaySeconds = kwargs["duration"]/len(text)
    cursor = kwargs.get("cursor")
    for c in text:
        sys.stdout.write(c+("|" if cursor else ""))
        sys.stdout.flush()
        sleep(delaySeconds)
        if cursor:
            sys.stdout.write("\b")
    sys.stdout.write(end)

delay_out("it", "works!", duration=3)

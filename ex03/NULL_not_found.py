from typing import Any


def NULL_not_found(object: Any) -> int:
    if object is None:
        print(f"Nothing : {object} {type(object)}")
    elif isinstance(object, float) and object != object:
        print(f"Garlic : {object} {type(object)}")
    elif object == 0:
        print(f"Zero : {object} {type(object)}")
    elif object == "":
        print(f"Empty : {object} {type(object)}")
    elif object is False:
        print(f"Fake : {object} {type(object)}")
    else:
        print(f"Type not found")
    return 42


Nothing = None
Garlic = float("NaN")
Zero = 0.0
Empty = ""
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))
if not float("NaN"):
    print("float('NaN') is False")

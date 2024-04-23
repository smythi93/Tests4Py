import sys
from thefuck.types import SortedCorrectedCommandsSequence
from thefuck.types import CorrectedCommand
from thefuck.types import Settings


if __name__ == "__main__":
    assert len(sys.argv) == 11

    expected = sys.argv[1]
    expected = expected[:-1]
    expected = expected[1:]

    script1 = sys.argv[2]
    script1 = script1[:-1]

    side_effect1 = sys.argv[3]
    side_effect1 = side_effect1[:-1]

    priority1 = sys.argv[4]
    priority1 = priority1[:-1]

    script2 = sys.argv[5]
    script2 = script2[:-1]

    side_effect2 = sys.argv[6]
    side_effect2 = side_effect2[:-1]

    priority2 = sys.argv[7]
    priority2 = priority2[:-1]

    script3 = sys.argv[8]
    script3 = script3[:-1]

    side_effect3 = sys.argv[9]
    side_effect3 = side_effect3[:-1]

    priority3 = sys.argv[10]
    priority3 = priority3[:-2]

    sort_corr_cmd_seq = SortedCorrectedCommandsSequence(iter(
        [CorrectedCommand(script1, side_effect1, priority1),
         CorrectedCommand(script2, side_effect2, priority2),
         CorrectedCommand(script3, side_effect3, priority3)]), Settings({'key': 'val'}))

    if priority1 == "None" or priority1 == "":
        print("Priority cannot be String or None")
    else:
        print(expected)

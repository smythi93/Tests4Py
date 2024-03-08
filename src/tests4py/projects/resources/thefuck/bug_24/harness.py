import sys
from thefuck.types import RulesNamesList
from thefuck.types import Rule


if __name__ == "__main__":
    assert len(sys.argv) == 4
    rule = sys.argv[1]
    rule = rule.replace("(", "")
    rule = rule[:-1]
    rules1 = sys.argv[2]
    rules1 = rules1.replace(",", "")
    rules1 = rules1.replace("[", "")
    rules2 = sys.argv[3]
    rules2 = rules2[:-2]
    if Rule(rule, "", "", "", "", "", "") in RulesNamesList((rules1, rules2)):
        print(rule)
    else:
        print("Rule is not in RulesNameList")

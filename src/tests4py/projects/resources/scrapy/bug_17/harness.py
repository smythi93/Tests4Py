import sys

# noinspection PyUnresolvedReferences
from scrapy.utils.response import response_status_message

if __name__ == "__main__":
    status = int(sys.argv[1])
    print(response_status_message(status))

import sys

# noinspection PyUnresolvedReferences
from scrapy.mail import MailSender

if __name__ == "__main__":
    mode = sys.argv[1]
    email = sys.argv[2]
    to = email if mode == "single" else [email]
    captured = {}

    def cb(**kw):
        captured["msg"] = kw["msg"]

    ms = MailSender(debug=True)
    ms.send(to=to, subject="subject", body="body", _callback=cb)
    print(captured["msg"]["To"])

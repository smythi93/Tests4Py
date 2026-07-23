import sys

from bin.wiki_entity_linking.wikipedia_processor import _process_wp_text


def main():
    mode = sys.argv[1]
    title = sys.argv[2]
    content = " ".join(sys.argv[3:])
    if mode == "extra":
        tag = '<text bytes="11456" xml:space="preserve">'
    else:
        tag = '<text xml:space="preserve">'
    article_text = tag + content + "</text>"
    clean_text, entities = _process_wp_text(title, article_text, {})
    print("RESULT:EXTRACTED" if clean_text is not None else "RESULT:NONE")


if __name__ == "__main__":
    main()

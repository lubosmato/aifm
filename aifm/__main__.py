from os import environ
from langchain_community.document_loaders import RecursiveUrlLoader


def main():
    environ["USER_AGENT"] = "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)  Googlebot 2.1"

    loader = RecursiveUrlLoader(
        "https://ui.shadcn.com/docs",
        max_depth=5,
    )
    docs = loader.load()

    print(f"Loaded {len(docs)} documents")
    for doc in docs:
        print(doc.metadata)

if __name__ == "__main__":
    main()


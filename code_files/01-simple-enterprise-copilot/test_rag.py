"""Console smoke test for policy retrieval."""

from rag import search_policies


def main() -> None:
    query = "What is annual leave carry forward limit?"
    print(f"Query: {query}\n")

    results = search_policies(query)

    if not results:
        print("No results returned. Run `python ingest.py` first.")
        return

    for idx, doc in enumerate(results, start=1):
        print(f"Result {idx}: {doc.metadata.get('source', 'Unknown')}")
        print(doc.page_content)
        print("-" * 40)


if __name__ == "__main__":
    main()

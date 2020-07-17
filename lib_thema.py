def display_item(data, level=0):
    pad = '  '*level
    print(f"{pad}{data['Omschrijving']} #{data['Id']}")
    for item in data['Items']:
        display_item(item, level + 1)


def display_docs(data):
    for doc in data['ResultatenLijst']:
        print(f"- {doc['Opschrift']}")
        print(f"    Id: {doc['Id']}")
        print(f"    Type: {doc['WetgevingDocumentType']}")
        print(f"    Datum: {doc['Datum']}")

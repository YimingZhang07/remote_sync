import nbformat
import pandas as pd
import re
import os


def readSingleIpynb(nbText):
    df = pd.DataFrame()
    section = "Missing"
    for cell in nbText['worksheets'][0]['cells']:
        if cell['cell_type'] == 'heading' and cell['level'] == 1:
            section = cell['source']
        if cell['cell_type'] == 'heading' and cell['level'] == 2:
            results = re.search(
                r"([0-9]*)\.\s([0-9A-Za-z\s]*)", cell['source'])
            if results is not None:
                record = {"Number": results.groups()[0], "Name": results.groups()[
                    1], "Section": section}
            else:
                record = {"Number": -1,
                          "Name": cell['source'], "Section": section}
            df = df.append(record, ignore_index=True)
    return df


def readFolderIpynb():
    df = pd.DataFrame()
    for file in os.listdir("./leetcode"):
        if file.endswith('ipynb') and file != "playground.ipynb":
            # change the path here if you move the script
            nb = nbformat.read("./leetcode/" + file, as_version=3)
            tmp = readSingleIpynb(nb)
            df = pd.concat([df, tmp], axis=0, ignore_index=True)

    df.Number = df.Number.astype('int32', errors='ignore')
    df = df.sort_values(by=["Section", "Number"]).reset_index(drop=True)
    return df


if __name__ == '__main__':
    df = readFolderIpynb()
    df.to_csv("leetcode_summary.csv", index=False)
    # change the path here to save in the development folder
    df.to_csv("../yimingzhang.net_UAT/content/top_project/leetcode/leetcode_summary.csv", index=True, index_label="Count")
    print("Success.")
import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

def generate_excel_from_urls(url_filename_pairs, combined_filename):
    all_dfs = []

    for url, filename in url_filename_pairs:
        response = requests.get(url)
        html_content = response.content

        soup = BeautifulSoup(html_content, "html.parser")
        table = soup.find("table", class_="table")

        if table:
            dfs = pd.read_html(StringIO(str(table)))

            if dfs:
                df = dfs[0]
                df.to_excel(filename, index=False)
                all_dfs.append(df)
                print(f"Excel file generated successfully: {filename}")
            else:
                print(f"No tables found on the webpage for URL: {url}")
        else:
            print(f"Table not found on the webpage for URL: {url}")

    # Combine all dataframes into a single DataFrame
    combined_df = pd.concat(all_dfs, ignore_index=True)

    # Write the combined DataFrame to a single sheet in the Excel file
    combined_df.to_excel(combined_filename, sheet_name='Combined', index=False)
    
    print(f"Combined Excel file generated successfully: {combined_filename}")

# List of URLs and filenames for individual Excel files
url_filename_pairs = [
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-369.htm", "table1_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-742.htm", "table2_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1680.htm", "table3_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-140.htm", "table4_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-582.htm", "table5_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1745.htm", "table6_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-805.htm", "table7_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3369.htm", "table8_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3620.htm", "table9_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3529.htm", "table10_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3165.htm", "table11_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1888.htm", "table12_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1420.htm", "table13_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-547.htm", "table14_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-772.htm", "table15_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1.htm", "table16_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-852.htm", "table17_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-860.htm", "table18_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-545.htm", "table19_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-804.htm", "table20_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1847.htm", "table21_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-544.htm", "table22_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1458.htm", "table23_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-834.htm", "table24_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1998.htm", "table25_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-83.htm", "table26_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-664.htm", "table27_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-911.htm", "table28_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1534.htm", "table29_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1142.htm", "table30_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3388.htm", "table31_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-2757.htm", "table32_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1584.htm", "table33_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-2484.htm", "table34_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-3482.htm", "table35_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1658.htm", "table36_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-1046.htm", "table37_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-2989.htm", "table38_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-2070.htm", "table39_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-160.htm", "table40_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-118.htm", "table41_report.xlsx"),
    ("https://results.eci.gov.in/PcResultGenJune2024/partywisewinresultState-743.htm", "table42_report.xlsx"),
]

# Combined Excel filename
combined_filename = "combined_report.xlsx"

generate_excel_from_urls(url_filename_pairs, combined_filename)
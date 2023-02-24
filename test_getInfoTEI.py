import unittest
import glob
import getInfoTEI as gitei
from pathlib import Path
from bs4 import BeautifulSoup

class TestGetInfoTEI(unittest.TestCase):
    
    def test_get_file_names(self):
        result = len(gitei.get_file_names())
        self.assertEqual(result, 10)

    def test_handle_requests(self):
        f = {'input': open("./Files/test/CCRB.pdf", 'rb')}
        response = gitei.handle_requests(f)
        self.assertNotEqual(response, False)

    def test_count_figures(self):
        f = {'input': open("./Files/test/CCRB.pdf", 'rb')}
        response = gitei.handle_requests(f)
        soup = BeautifulSoup(response.content, "xml")
        figures = soup.find_all("figure")
        print(len(figures))
        self.assertEqual(len(figures), 3)



    def test_main(self):
        gitei.main()
        input_files = glob.glob("./Files/PDFs/*.pdf")
        input_files =[Path(file).stem for file in input_files]
        input_files.append("barChart")
        output_files = glob.glob("./Files/output/*.png")
        output_files = [Path(file).stem for file in output_files]

        self.assertTrue(set(input_files) == set(output_files))

if __name__ == "__main__":
    unittest.main()
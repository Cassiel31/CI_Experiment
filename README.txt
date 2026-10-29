LAB 9: INTRODUCTION TO CONTINUOUS INTEGRATION (CI)

PROJECT FILES
- calculator.py
- test_calculator.py
- .github/workflows/ci.yml

PART 1: RUN TESTS LOCALLY
1. Extract the ZIP.
2. Open the CI_Experiment folder in VS Code.
3. Open Terminal > New Terminal.
4. Run:
   python -m unittest -v
5. Expected: Ran 3 tests ... OK.

PART 2: UPLOAD TO GITHUB
1. Create a GitHub repository named CI_Experiment.
2. Upload calculator.py and test_calculator.py to the repository root.
3. Create the workflow file at this exact path:
   .github/workflows/ci.yml
   On GitHub, use Add file > Create new file and enter the path including folders.
4. Commit the files. The push should automatically trigger GitHub Actions.

PART 3: CHECK THE WORKFLOW
1. Open the repository's Actions tab.
2. Select Python CI and open the latest run.
3. Capture the successful workflow and the step showing all 3 tests passed.

PART 4: INTRODUCE A DEFECT
1. Temporarily change calculator.py to:
   def add(a, b):
       return a - b
2. Commit the change to GitHub.
3. Open Actions and capture the failed workflow run. The addition tests should fail.
4. Restore calculator.py:
   def add(a, b):
       return a + b
5. Commit the correction and check Actions again. Capture the successful workflow run.

SCREENSHOTS TO TAKE
1. VS Code Explorer showing calculator.py, test_calculator.py, and .github/workflows/ci.yml.
2. calculator.py code.
3. test_calculator.py code.
4. Terminal output of `python -m unittest -v` showing 3 tests and OK.
5. GitHub repository showing the uploaded files.
6. GitHub Actions successful run after the workflow is added.
7. GitHub Actions failed run after temporarily changing addition to subtraction.
8. GitHub Actions successful run after restoring the correct code.

IMPORTANT
- The workflow runs when changes are pushed to GitHub.
- Python's built-in unittest is used, so no third-party test package is needed.
- Do not leave the intentional subtraction defect in your final repository. Restore addition and push it.

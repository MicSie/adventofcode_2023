import os
import shutil


def create_new_day():
    path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
    new_day = len([1 for dirname in os.listdir(path) if dirname.startswith("day")]) + 1
    new_day_string = f"day{format(new_day, '02d')}"
    print(f"creating {new_day_string}")
    template_path = os.path.join(path, "template")
    newday_path = os.path.join(path, new_day_string)
    print(f"{template_path} => {newday_path}")
    shutil.copytree(template_path, newday_path)

    test_input_file = open(
        os.path.join(path, "tests", "inputs", f"{new_day_string}.txt"), "w"
    )
    test_input_file.close()

    with open(
        os.path.join(path, "tests", f"{new_day_string}_test.py"), "w"
    ) as test_file:
        test_file.writelines(
            [
                f"import {new_day_string}.task as task  # The code to test\n",
                "import unittest  # The test framework\n",
                "import os\n",
                "import basics\n",
                "\n",
                f"class Test_D{str(new_day_string[1:])}(unittest.TestCase):\n",
                "    def setUp(self):\n",
                f'        self.input_lines = basics.read_file(os.path.abspath("tests/inputs/{new_day_string}.txt"))\n',
                "\n",
                "    def test_part1(self):\n",
                "        self.assertTrue(True)\n",
                "\n",
                "    def test_part2(self):\n",
                "        self.assertTrue(True)\n",
                "\n",
                'if __name__ == "__main__":',
                "    unittest.main()\n",
            ]
        )

    with open(os.path.join(path, "tests", "context.py"), "a") as context_file:
        context_file.write(f"import {new_day_string}\n")

    with open(os.path.join(path, "run_all.py"), "r") as run_all:
        text = run_all.read()

    old_day = f"day{format(new_day-1, '02d')}"
    text = text.replace(
        f"import {old_day}", f"import {old_day}\nimport {new_day_string}"
    )
    text = text.replace(
        f"{old_day}.run_day()", f"{old_day}.run_day()\n    {new_day_string}.run_day()"
    )
    with open(os.path.join(path, "run_all.py"), "w") as run_all:
        run_all.write(text)

    with open(os.path.join(path, new_day_string, "task.py"), "r") as task_file:
        text = task_file.read()

    text = text.replace("DayXX", f"D{new_day_string[1:]}")
    with open(os.path.join(path, new_day_string, "task.py"), "w") as task_file:
        task_file.write(text)


if __name__ == "__main__":
    create_new_day()

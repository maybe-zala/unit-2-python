import unittest

from main import *

class TestFunctions(unittest.TestCase):

    def test_module_progress_class(self):
        progress=ModuleProgress()
        self.assertEqual(progress.state, "Introductory Exercises")
        self.assertEqual(progress.attempts, 0)

    def test_complete_task_function(self):
        progress=ModuleProgress()
        complete_task(progress)
        self.assertEqual(progress.state, "Project")
        complete_task(progress)
        self.assertEqual(progress.state, "Benchmark")
        complete_task(progress)
        self.assertEqual(progress.state, "Benchmark")

    def test_pass_task_function(self):
        progress=ModuleProgress()
        progress.state = "Benchmark"
        pass_task(progress)
        self.assertEqual(progress.state, "Module Complete")

        progress2=ModuleProgress()
        pass_task(progress2)
        self.assertEqual(progress2.state, "Introductory Exercises")
    
    def test_fail_task_function(self):
        progress=ModuleProgress()
        progress.state = "Benchmark"
        fail_task(progress)
        self.assertEqual(progress.state, "Project")
        self.assertEqual(progress.attempts, 1)

        progress2=ModuleProgress()
        fail_task(progress2)
        self.assertEqual(progress2.state, "Introductory Exercises")

        progress3=ModuleProgress()
        progress3.state = "Benchmark"
        progress3.attempts = 2
        fail_task(progress3)
        self.assertEqual(progress3.state, "Failed")

if __name__ == '__main__':
    unittest.main()
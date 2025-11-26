## Quality Development starter pack

This repository has been created to give a python template project which includes pytest instructions.

### 1️⃣ How to start (one-time step)

Fork this repository and clone your fork into your machine using:

```bash
git clone git@github.com:USERNAME/qd-starter-pack.git
```

enter to your project directory using:

```bash
cd qd-starter-pack
```

Setup virtualenv:

```bash
python3 -m pip install venv
python3 -m venv venv
source ./venv/bin/activate
```

After running these commands you'll see a `(venv)` in your terminal, if so, you are running the python version of the local environment.

Then, install the tests requirements in your local virtual environment

```bash
pip install -r requirements_dev.txt
```

⚠️ Note: You need to run `source ./venv/bin/activate` every time you open a new terminal to activate the local virtual environment.

---

### 2️⃣ How to make a branch

To create a new `branch` from the main repository and work on a specific exercise (ex. `ex1.py`) you can use the following commands:

```bash
git checkout main

git checkout -b new-branch-name
```

---

### 3️⃣ How to make a commit

From this step you can edit your `ex1.py` and make some commits using:

```bash
git add src/ex1.py

git commit -m 'feat: description'
```

Use the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) when you write a commit description.

---

### 4️⃣ How to make a PR

Push the commits into GitHub using:

```bash
git push -u origin new-branch-name
```

Afterward, it is possible to create a Pull Request by going to your fork `https://github.com/USERNAME/qd-starter-pack.git` clicking on "create Pull Request" or going to the right section "Pull Request" -> "New Pull Request".

If you want to work on another `ex1.py`, go to step 2️⃣.

---

Use git wisely.

### Software Testing

How to run properly the tests with the related html report:

```bash
$ pytest --cov src tests/ --cov-report=html

# or

$ pytest .
```

### Clean code

Check [this article](https://testdriven.io/blog/clean-code-python/) to understand how to write "clean code" in python.

### Contributing

Feel free to improve this README with any other detail, if you do it, I'll be grateful.

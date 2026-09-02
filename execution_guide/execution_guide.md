## [HabitSync — Execution Guide]()

<br><br>

### [***A super simple guide, written for a 12-year-old!***]
<br>

Hi! 👋 This guide will help you run **HabitSync** on your computer, one tiny
step at a time. HabitSync is a smart little program that helps a couple pick
healthy food and gym products, and it can even **talk out loud** using a
computer voice!

You don't need to understand everything — just follow the steps **in
order**, copy the gray boxes exactly, and paste them into the Terminal. That's it!

<br><br>

## [Step 0 — What is the Terminal?]()
<br><br>

### [***A window where you type commands instead of clicking***]
<br>

On a Mac, the **Terminal** is an app where you type words instead of
clicking buttons. It looks a bit scary the first time, but it's really just
a way to *tell your computer what to do*, one line at a time.

**How to open it:**

1. Press `Command (⌘) + Space` on your keyboard.
2. Type: `Terminal`
3. Press `Enter`.

A dark or white window will pop up with some text and a blinking cursor.
That's your Terminal, ready for commands! 🎉

<br><br>

## [Step 1 — Go to the HabitSync folder]()
<br><br>

### [***Tell the Terminal where the project lives***]
<br>

Copy this, paste it into the Terminal, and press `Enter`:

```bash
cd /Users/fabicampanari/Desktop/4-Project_HabitSync
```

`cd` means "change directory" — you're just telling the Terminal:
*"Hey, go into this folder!"*

✅ **You'll know it worked if:** nothing bad happens (no red error text) and
the Terminal is just waiting for your next command.

<br><br>

## [Step 2 — Check that Python is installed]()
<br><br>

### [***Python is the language HabitSync is written in***]
<br>

Copy and paste this:

```bash
python3 --version
```

✅ **You should see something like:** `Python 3.12.3`

❌ **If you see "command not found"**, that means Python isn't installed
yet. Ask a grown-up to help you install it from
[python.org](https://www.python.org/downloads/), then come back to this
step.

<br><br>

## [Step 3 — Install the tools HabitSync needs]()
<br><br>

### [***Like installing apps, but for code***]
<br>

HabitSync needs a few helper tools to work. Copy and paste this:

```bash
python3 -m pip install -r requirements.txt
```

✅ **You should see:** a bunch of text scrolling by, ending with something
like `Successfully installed pandas numpy gTTS`.

❌ **If you see an error that mentions "externally-managed-environment"**,
don't worry! Just copy and paste this instead:

```bash
python3 -m pip install -r requirements.txt --break-system-packages
```

<br><br>

## [Step 4 — Install Jupyter (so we can run the notebook)]()
<br><br>

### [***One more helper tool***]
<br>

Copy and paste this:

```bash
python3 -m pip install jupyter nbconvert
```

(If you get the same "externally-managed-environment" error as before, just
add `--break-system-packages` at the end again, like in Step 3.)

<br><br>

## [Step 5 — Create the pretend data]()
<br><br>

### [***HabitSync needs some example products and people to work with***]
<br>

Copy and paste this:

```bash
python3 scripts/generate_synthetic_data.py
```

✅ **You should see:**

```
[OK] validate_dataset: todas as verificações passaram.

products: (28, 12) | users: (24, 7) | interactions: (180, 7)
couples: 12 (incluindo 2 casais de demonstração)
```

That means your computer just created 28 pretend products and 12 pretend
couples, all by itself! 🎁

<br><br>

## [Step 6 — Run HabitSync for real!]()
<br><br>

### [***This is the fun part***]
<br>

Copy and paste this (it's actually 3 commands in a row — that's okay, just
paste all of it at once):

```bash
cd notebooks
jupyter nbconvert --to script habitsync_mvp.ipynb
python3 habitsync_mvp.py
```

This turns the notebook into a plain program and runs it, right there in
the Terminal.

✅ **You should see a LOT of text**, including lines that start with `[OK]`,
some example recommendations, and — at the very end — this exact message:

```
NB COMPLETED SUCCESSFULLY — READY FOR next NB
```

If you see that message, **you did it!** 🥳

<br><br>

## [Step 7 — Where are my results?]()
<br><br>

### [***Your computer saved some files for you***]
<br>

Go back to the main folder:

```bash
cd ..
```

Inside `data/synthetic/`, you'll find 3 files you can open like a
spreadsheet (double-click them, or open with Excel/Numbers):

- `products.csv` — the pretend products
- `users.csv` — the pretend couples
- `interactions.csv` — pretend shopping history

If your Terminal supported audio, you might also find a file called
`habitsync_audio.mp3` inside `notebooks/` — that's the computer's voice
saying a recommendation out loud!

<br><br>

## [Uh oh! Something went wrong 🛟]()
<br><br>

### [***Don't panic — here's what common errors mean***]
<br>

| What you see | What it means | What to do |
|---|---|---|
| `command not found: python` | Your Mac wants `python3`, not `python` | Always type `python3`, not `python` |
| `command not found: pip` | Same idea | Use `python3 -m pip` instead of just `pip` |
| Red text mentioning `externally-managed-environment` | Your Mac is being extra careful | Add `--break-system-packages` to the end of the command |
| `No such file or directory` | You're in the wrong folder | Go back to Step 1 and run the `cd` command again |

<br><br>

## [You did it! 🎉]()
<br><br>

### [***HabitSync is now running on your computer***]
<br>

You just installed tools, generated data, and ran a real AI recommendation
project — all by typing into a Terminal like a real programmer. Great job!

import random


class Wordle:
    """
    A Wordle-style word guessing game Class.

    The game allows a user to guess a 5-letter word, providing feedback on correct and incorrect letters.
    Hints reveal specific letters in a structured manner.

    .. code-block:: python
       :caption: Example Usage

        api = Wordle()

        # Start a game
        result = await api.start(key=1234, hint_limit=3, attempt_limit=5)
        print(result)

        # Make a guess
        result = await api.guess(key=1234, word="apple")
        print(result)

        # Request a hint
        result = await api.hint(key=1234)
        print(result)

        # End the game
        result = await api.end(key=1234)
        print(result)

    ..code-block:: JSON
       :caption: Expected Outputs

        {'status': 'success', 'message': 'Game started! Guess a 5-letter word.', 'rules': {...}, 'hints_left': 3, 'attempts_left': 5}
        {'status': 'continue', 'hint': '🟩⬛🟨⬛⬛', 'attempts_left': 4}
        {'status': 'success', 'message': 'This is your 1st hint: The 3️⃣ character of the word is `L`', 'hints_left': 2}
        {'status': 'ended', 'message': 'Game ended. The word was "melon".'}
    """

    def __init__(self):
        self.active_games = {}

    async def start(self, key: int, hint_limit: int = 3, attempt_limit: int = 5):
        """
        Start a new Wordle game.

        Args:
            key (``int``): Unique game identifier.
            hint_limit (``int``): Max hints allowed (default: 3).
            attempt_limit (``int``): Max attempts allowed (default: 5).

        Returns:
            dict: Game start details.

        Example:

            ..code-block:: python

                result = await api.start(key=1234, hint_limit=3, attempt_limit=5)
                print(result)

            ..code-block:: JSON
               :caption: Expected Output

               {
                    'status': 'success',
                    'message': 'Game started! Guess a 5-letter word.',
                    'rules': {
                        '🟩': 'Correct letter in correct position',
                        '🟨': 'Correct letter in wrong position',
                        '⬛': 'Incorrect letter'
                     },
                    'hints_left': 3,
                    'attempts_left': 5
                }
        """
        if key in self.active_games:
            return {"status": "error", "message": "Game already in progress!"}

        from .api import Client

        words = await Client().get_words()
        secret_word = random.choice(words)
        self.active_games[key] = {
            "word": secret_word,
            "attempts": 0,
            "attempt_limit": attempt_limit,
            "hints_used": 0,
            "hint_limit": hint_limit,
            "hint_positions": [],
        }

        return {
            "status": "success",
            "message": "Game started! Guess a 5-letter word.",
            "rules": {
                "🟩": "Correct letter in correct position",
                "🟨": "Correct letter in wrong position",
                "⬛": "Incorrect letter",
            },
            "hints_left": hint_limit,
            "attempts_left": attempt_limit,
        }

    async def guess(self, key: int, word: str):
        """
        Process a user's guess and return feedback.

        Args:
            key (``int``): Game identifier.
            word (``str``): The guessed word (must be 5 letters).

        Returns:
            dict: Feedback on the guess or game end status.

        Color Explanation:
        - 🟩 (``Green``): Correct letter in the correct position.
        - 🟨 (``Yellow``): Correct letter in the wrong position.
        - ⬛ (``Black``): Letter is not in the word.

        Example:

            ..code-block:: python
               :caption: Example Usage

                result = await api.guess(key=1234, word="apple")
                print(result)

            ..code-block:: JSON
               :caption: Expected Output

                {
                    'status': 'continue',
                    'hint': '🟩⬛🟨⬛⬛',
                   'attempts_left': 4
                }
        """
        if key not in self.active_games:
            return {"status": "error", "message": "No active game!"}

        game = self.active_games[key]

        if len(word) != 5 or not word.isalpha():
            return {
                "status": "error",
                "message": "Guess must be a valid 5-letter word!",
            }

        game["attempts"] += 1

        if game["attempts"] > game["attempt_limit"]:
            return await self.end(key, exceeded=True)

        hint = self._generate_hint(game["word"], word)

        if word == game["word"]:
            return await self.end(key, win=True)

        return {
            "status": "continue",
            "hint": hint,
            "attempts_left": game["attempt_limit"] - game["attempts"],
        }

    async def hint(self, key: int):
        """
        Provide a structured hint.

        Args:
            key (``int``): Game identifier.

        Returns:
            dict: A structured hint message or an error if no hints remain.

        Example:

            ..code-block :: python

                result = await api.hint(key=1234)

                print(result)

            ..code-block :: JSON
               :caption: Expected Output

                {'status': 'success', 'message': 'This is your 1st hint: The 3️⃣ character of the word is `L`', 'hints_left': 2}
        """
        if key not in self.active_games:
            return {"status": "error", "message": "No active game!"}

        game = self.active_games[key]

        if game["hints_used"] >= game["hint_limit"]:
            return {"status": "error", "message": "You've used all hints!"}

        hint_text, game["hint_positions"] = self._get_incremental_hint(
            game["word"], game["hint_positions"]
        )

        if hint_text:
            game["hints_used"] += 1
            return {
                "status": "success",
                "message": f"This is your {game['hints_used']} hint: {hint_text}",
                "hints_left": game["hint_limit"] - game["hints_used"],
            }

        return {"status": "error", "message": "No more hints available!"}

    async def end(self, key: int, exceeded: bool = False, win: bool = False):
        """
        End the game and reveal the correct word.

        Args:
            key (``int``): Game identifier.
            exceeded (``bool``): Whether the game ended due to exceeding attempts.
            win (``bool``): Whether the user won.

        Returns:
            dict: Game result and correct answer.

        Example:
            ..code-block :: python

                result = await api.end(key=1234)
                print(result)

            ..code-block :: JSON
               :caption: Expected Output

                {'status': 'ended', 'message': 'Game ended. The word was "melon".'}
        """
        if key in self.active_games:
            word = self.active_games[key]["word"]
            del self.active_games[key]

            if win:
                return {
                    "status": "win",
                    "message": f"You guessed it! The word was '{word}'.",
                }

            if exceeded:
                return {
                    "status": "lost",
                    "message": f"You exceeded your limit! The correct word was '{word}'.",
                }

            return {"status": "ended", "message": f"Game ended. The word was '{word}'."}

        return {"status": "error", "message": "No active game to end."}

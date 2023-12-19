"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started

dragon_story = Story(
    ["color", "superlative_ending_in_est", "adjective_1", "body_part_plural", "body_part", "noun", "animal_plural", "adjective_2", "adjective_3", "adjective_4"],
    """The {color} Dragon is the {superlative_ending_in_est} Dragon of all. It has {adjective_1} {body_part_plural}, and a {body_part} shaped like a {noun}. It loves to eat {animal_plural}, although it will feast on nearly anything. It is {adjective_2} and {adjective_3}. You must be {adjective_4} around it, or you may end up as its meal!"""
)

bat_story = Story(
    ["color", "adjective_1", "time", "adjective_2", "place", "food_1", "food_2", "verb", "person", "number"],
    """Bats are so cool! They are {color}, {adjective_1} animals which have wings. They like to fly around at {time} which makes some people scared of them. But bats are {adjective_2}, and they don't want to hurt people. I have a pet bat that lives in {place}. I like to feed him {food_1} and {food_2}. He likes to {verb}. I am his favorite person, but he also likes {person}. I want to convince my parents to get me {number} more bats."""
)

doctor_story = Story(
    ["adjective_1", "place_1", "adjective_2", "adjective_3", "piece_of_clothing", "body_part_1", "body_part_2", "body_part_3", "adjective_4", "noun_1", "noun_2", "place_2", "adjective_5"],
    """Every year, you should go visit the doctor. It is a very {adjective_1} visit. Usually, you have to skip going to {place_1} to go. Your doctor is usually a/an {adjective_2} man or woman who is wearing a/an {adjective_3} {piece_of_clothing}. They will look at your {body_part_1}, {body_part_2}, and {body_part_3}. Sometimes, they can be very {adjective_4}. Afterwards, they will give you a {noun_1} and a {noun_2} and your mom or dad will take you to {place_2} as a treat. All in all, the doctor's office isn't so {adjective_5}!""")

store_story = Story(
    ["holiday", "name_1", "verb_1", "store_name", "noun_1", "adjective_1", "noun_2", "adjective_2", "noun_3", "adjective_3", "noun_4", "name_2", "verb_2", "verb_3", "adjective_4", "type_of_store"],
    """It was almost {holiday}, so {name_1} knew they had to go grocery shopping. They {verb_1} to the {store_name} and picked up a {noun_1}. They looked at their list. They needed to get {adjective_1} {noun_2}, {adjective_2} {noun_3}, and {adjective_3} {noun_4}. They couldn't find anything! Eventually they saw their friend, {name_2}, and {verb_2} them for help. Their friend {verb_3}. "You're in the {adjective_4} place!" they said. "This is a {type_of_store}!"""
)

stories = {"dragon": dragon_story, "bat": bat_story, "doctor": doctor_story, "store": store_story}
from aiogram.utils.keyboard import InlineKeyboardMarkup, InlineKeyboardBuilder
from typing import List, Union
from itertools import zip_longest


def inline_builder(
        text: Union[str, List[str]],
        callback_data: Union[str, List[str]],
        sizes: Union[int, List[int]] = 1
) -> InlineKeyboardMarkup:
    """
    Builds an inline keyboard using given text and callback data.

    :param text: Text for each button (single string or list of strings).
    :param callback_data: Callback data for each button (single string or list of strings).
    :param sizes: Number of buttons per row (single integer or list of integers, default is 1).
    :return: InlineKeyboardMarkup object.
    """
    builder = InlineKeyboardBuilder()

    if isinstance(text, str):
        text = [text]
    if isinstance(callback_data, str):
        callback_data = [callback_data]
    if isinstance(sizes, int):
        sizes = [sizes]

    if len(text) != len(callback_data):
        raise ValueError("Length of text and callback_data must be the same.")

    for txt, cb in zip_longest(text, callback_data):
        if txt is not None and cb is not None:
            builder.button(text=txt, callback_data=cb)
        else:
            raise ValueError("Mismatch in lengths of text and callback_data lists.")

    builder.adjust(*sizes)
    return builder.as_markup()

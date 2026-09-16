from src.library.library import Library


def before_scenario(context, scenario):
    """
    Adds a library object to context
    """
    context.library = Library()

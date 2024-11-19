from functools import wraps


class StartupManager:
    tasks = {"init": [], "dispose": []}

    @classmethod
    def onStart(cls, order):
        """Class-level decorator for startup tasks."""
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            cls.tasks["init"].append((order, wrapper))
            return wrapper
        return decorator

    @classmethod
    def onEnd(cls, order):
        """Class-level decorator for disposal tasks."""
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            cls.tasks["dispose"].append((order, wrapper))
            return wrapper
        return decorator

    @classmethod
    def execute_init_tasks(cls, context):
        """Execute startup tasks."""
        for _, task in sorted(cls.tasks["init"], key=lambda x: x[0]):
            task(context)

    @classmethod
    def execute_dispose_tasks(cls, context):
        """Execute disposal tasks."""
        for _, task in sorted(cls.tasks["dispose"], key=lambda x: x[0]):
            task(context)

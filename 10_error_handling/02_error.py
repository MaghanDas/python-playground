

# Custom Exception

class AppError(Exception):
    pass 

class ValidationError(AppError):
    """Raise when input data is invalid"""
    def __init__(self, field:str, message:str):
        self.field = field 
        self.message = message 
        super().__init__(f"Validation failed on '{field}' : {message}")

class NotFoundError(AppError):
        """Raise when a resource doesn't exist """
        def __init__(self, ):

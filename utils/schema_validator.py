from jsonschema import validate, ValidationError

class SchemaValidator:
    """Reusable schema validation class."""

    @staticmethod
    def validate_json(response_json, schema):
        """Validates a JSON response against a schema."""
        try:
            validate(instance=response_json, schema=schema)
            return True
        except ValidationError as e:
            # Extracting the path to the failing property
            error_path = " → ".join(map(str, e.path)) if e.path else "Root"
            print(f"❌ JSON Schema Validation Failed: {error_path} → {e.message}")
            return False
import os
from mlProject import logger
import pandas as pd
from mlProject.entity.config_entity import DataValidationConfig

class DataValidation:
    def __init__(self, config):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            # Normalize and clean up the file path
            file_path = os.path.normpath(self.config.unzip_data_dir.strip('"'))  # Removes extra quotes
            
            print(f"📌 Using file path: {file_path}")  # Debugging print

            if not os.path.exists(file_path):
                raise FileNotFoundError(f"❌ File not found: {file_path}")

            # Read the file
            data = pd.read_csv(file_path)
            all_cols = list(data.columns)
            all_schema = self.config.all_schema.keys()

            validation_status = all(col in all_schema for col in all_cols)

            # Ensure status file directory exists
            status_file = os.path.normpath(self.config.STATUS_FILE)
            os.makedirs(os.path.dirname(status_file), exist_ok=True)

            # Write validation status
            with open(status_file, 'w') as f:
                f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise e
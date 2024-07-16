import json
from typing import Any, Dict, List, Tuple, Optional

import hello.settings

PROJECT_MANAGEMENT_DATA_QUESTIONS = hello.settings.BASE_DIR / 'projectmanagement/data/questions.json'


def import_questions() -> Tuple[Optional[Exception], List[Dict[str, Any]]]:
    try:
        with open(PROJECT_MANAGEMENT_DATA_QUESTIONS) as json_file:
            data = json.load(json_file)
            return None, data
    except Exception as e:
        return e, []

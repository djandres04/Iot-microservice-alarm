from utils import ConverterTime

status = False


class alarm:
    def __init__(self, id, description=None, date_alarm=None, person=None) -> None:
        self.id = id,
        self.description = description
        self.status = status
        self.date_alarm = date_alarm
        self.person = person

    def to_JSON(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "date_created": ConverterTime.time_now(),
            "date_alarm": self.date_alarm,
            "person": self.person
        }

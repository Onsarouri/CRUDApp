from pydantic import BaseModel, ConfigDict
from datetime import datetime

# these models validate incoming data to ensure it conforms to the defined schema

#schema for returning a note
class NoteModel(BaseModel):

    id : str
    title :str
    content: str
    date_created : datetime

    model_config = ConfigDict(
        from_attributes= True
    )

#creating new note objects through an API endpoint where data is received in JSON format
#schema for creating a note
class NoteCreateModel(BaseModel):
    title :str
    content: str

    model_config = ConfigDict(
        from_attributes= True,
        json_schema_extra={
            "example":{
                "title":"Sample title",
                "content" : "Sample content"
            }
        }
    )

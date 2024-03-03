from flask_pymongo import PyMongo

mongo = PyMongo()

# Overlay Model
class Overlay:
    def __init__(self, position, size, content):
        self.position = position
        self.size = size
        self.content = content

    def to_dict(self):
        return {
            "position": self.position,
            "size": self.size,
            "content": self.content
        }

    @classmethod
    def from_dict(cls, data):
        return cls(**data)

# from flask_pymongo import PyMongo

# mongo = PyMongo()

# def create_overlay(overlay_data):
#     mongo.db.overlays.insert_one(overlay_data)

# def get_overlay(overlay_id):
#     return mongo.db.overlays.find_one({'_id': overlay_id})

# def update_overlay(overlay_id, overlay_data):
#     mongo.db.overlays.update_one({'_id': overlay_id}, {'$set': overlay_data})

# def delete_overlay(overlay_id):
#     mongo.db.overlays.delete_one({'_id': overlay_id})

"""BlogTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Blog import Blog

class BlogTableSeeder(Seeder):
    def run(self):
        """Run the database seeds."""
        Blog.create({"title": "Blog1", "body": "What's up, everyone!"})
        Blog.create({"title": "Blog2", "body": "Hey, everyone!"})
        Blog.create({"title": "Blog3", "body": "YO, everyone!"})

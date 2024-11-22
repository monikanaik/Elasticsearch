from django.core.management.base import BaseCommand
from faker import Faker

from app.models import Book


class Command(BaseCommand):
    help = "Populate the Book model with fake data"

    def handle(self, *args, **kwargs):
        fake = Faker()
        books = []

        for _ in range(1000):
            books.append(
                Book(
                    title=fake.sentence(nb_words=5),
                    author=fake.name(),
                    description=fake.paragraph(nb_sentences=3),
                )
            )

        # Bulk create for performance optimization
        Book.objects.bulk_create(books)
        self.stdout.write(self.style.SUCCESS("Successfully added 1000 books"))

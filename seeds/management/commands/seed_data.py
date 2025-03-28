import random
from faker import Faker
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from lloguer.models import Automobil, Reserva
from datetime import timedelta

fake = Faker()

class Command(BaseCommand):
    help = "Crea datos de prueba en la base de datos sin eliminar los existentes"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS("✔ Cargando datos de prueba..."))

        # Crear 4 Automòbils
        automobils = []
        for _ in range(4):
            auto = Automobil.objects.create(
                marca=fake.company(),
                model=fake.word(),
                matricula=fake.unique.license_plate()
            )
            automobils.append(auto)

        self.stdout.write(self.style.SUCCESS("✔ 4 Automòbils creats."))

        # Crear 8 Usuaris
        users = []
        for _ in range(8):
            username = fake.unique.user_name()
            user = User.objects.create_user(username=username, password="password123")
            users.append(user)

        self.stdout.write(self.style.SUCCESS("✔ 8 Usuaris creats."))

        # Crear Reserves (1 o 2 por usuario)
        for user in users:
            num_reserves = random.randint(1, 2)
            for _ in range(num_reserves):
                automobil = random.choice(automobils)
                data_inici = fake.date_between(start_date="-30d", end_date="+30d")
                data_fi = data_inici + timedelta(days=random.randint(1, 7))

                Reserva.objects.create(
                    automobil=automobil,
                    user=user,
                    data_inici=data_inici,
                    data_fi=data_fi
                )

        self.stdout.write(self.style.SUCCESS("✔ Reserves creades correctament."))

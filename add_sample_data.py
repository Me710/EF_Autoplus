#!/usr/bin/env python3
"""
Script pour ajouter des données d'exemple à la base de données EF AUTO+
"""

from app import app, db, Vehicle
from datetime import datetime

def add_sample_vehicles():
    """Ajoute des véhicules d'exemple à la base de données"""
    
    sample_vehicles = [
        {
            'name': 'Toyota Camry 2021',
            'type': 'sedan',
            'price': '25,900$',
            'image_url': 'https://images.unsplash.com/photo-1541899481282-d53bffe3c35d?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1740&q=80',
            'description': 'Berline familiale fiable et économique. Excellent état, entretien régulier.',
            'year': 2021,
            'mileage': '45,000 km',
            'fuel_type': 'Essence',
            'transmission': 'Automatique'
        },
        {
            'name': 'Ford Explorer 2022',
            'type': 'suv',
            'price': '36,500$',
            'image_url': 'https://images.unsplash.com/photo-1606744837616-56c9a5c6a6eb?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1742&q=80',
            'description': 'SUV spacieux et polyvalent. Parfait pour la famille et les activités extérieures.',
            'year': 2022,
            'mileage': '32,000 km',
            'fuel_type': 'Essence',
            'transmission': 'Automatique'
        },
        {
            'name': 'RAM 1500 2020',
            'type': 'truck',
            'price': '32,700$',
            'image_url': 'https://images.unsplash.com/photo-1570681950018-cc01b0df03a3?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1740&q=80',
            'description': 'Camion robuste et puissant. Idéal pour le travail et les loisirs.',
            'year': 2020,
            'mileage': '58,000 km',
            'fuel_type': 'Essence',
            'transmission': 'Automatique'
        },
        {
            'name': 'BMW X5 2022',
            'type': 'luxury',
            'price': '59,900$',
            'image_url': 'https://images.unsplash.com/photo-1616788494707-ec28f08fd05a?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1740&q=80',
            'description': 'SUV de luxe avec toutes les options. Performance et confort exceptionnels.',
            'year': 2022,
            'mileage': '28,000 km',
            'fuel_type': 'Essence',
            'transmission': 'Automatique'
        },
        {
            'name': 'Honda Civic 2020',
            'type': 'sedan',
            'price': '21,300$',
            'image_url': 'https://images.unsplash.com/photo-1558981852-426c6c22a060?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1742&q=80',
            'description': 'Compacte économique et fiable. Parfaite pour la ville et les déplacements quotidiens.',
            'year': 2020,
            'mileage': '52,000 km',
            'fuel_type': 'Essence',
            'transmission': 'Manuelle'
        },
        {
            'name': 'Jeep Grand Cherokee 2021',
            'type': 'suv',
            'price': '38,200$',
            'image_url': 'https://images.unsplash.com/photo-1591462658157-2c227bbf1c50?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1740&q=80',
            'description': 'SUV tout-terrain avec capacités hors route exceptionnelles.',
            'year': 2021,
            'mileage': '41,000 km',
            'fuel_type': 'Essence',
            'transmission': 'Automatique'
        },
        {
            'name': 'Mercedes-Benz C-Class 2021',
            'type': 'luxury',
            'price': '42,800$',
            'image_url': 'https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1740&q=80',
            'description': 'Berline de luxe avec finition premium et technologies avancées.',
            'year': 2021,
            'mileage': '35,000 km',
            'fuel_type': 'Essence',
            'transmission': 'Automatique'
        },
        {
            'name': 'Chevrolet Silverado 2020',
            'type': 'truck',
            'price': '29,500$',
            'image_url': 'https://images.unsplash.com/photo-1563720223185-11003d516935?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=1740&q=80',
            'description': 'Camion américain robuste avec grande capacité de remorquage.',
            'year': 2020,
            'mileage': '65,000 km',
            'fuel_type': 'Essence',
            'transmission': 'Automatique'
        }
    ]
    
    with app.app_context():
        # Vérifier si des véhicules existent déjà
        existing_count = Vehicle.query.count()
        if existing_count > 0:
            print(f"⚠️  {existing_count} véhicules existent déjà dans la base de données.")
            response = input("Voulez-vous ajouter les véhicules d'exemple quand même ? (o/n): ")
            if response.lower() != 'o':
                print("❌ Opération annulée.")
                return
        
        # Ajouter les véhicules
        for vehicle_data in sample_vehicles:
            vehicle = Vehicle(**vehicle_data)
            db.session.add(vehicle)
        
        db.session.commit()
        print(f"✅ {len(sample_vehicles)} véhicules d'exemple ajoutés avec succès !")
        print("\nVéhicules ajoutés :")
        for vehicle in sample_vehicles:
            print(f"  - {vehicle['name']} ({vehicle['price']})")

if __name__ == '__main__':
    print("🚗 Ajout de véhicules d'exemple à EF AUTO+")
    print("=" * 50)
    add_sample_vehicles()
    print("\n🎉 Script terminé !")
    print("Vous pouvez maintenant lancer l'application avec : python app.py") 
from flask_restful import Resource

hoteis = [
            {
                'hotel_id': 'chalie',
                'name': 'Charlie Hotel',
                'estrela': '3.9',
                'diaria': '420',
                'cidade': 'Campina Grande'                
            },
            {
                'hotel_id': 'Nord',
                'name': 'Nord Hotel',
                'estrela': '4',
                'diaria': '650',
                'cidade': 'Campina Grande'                
            },
            {
                'hotel_id': 'alpha',
                'name': 'Alpha Hotel',
                'estrela': '5',
                'diaria': '800',
                'cidade': 'Campina Grande'                
            }
            
]



class Hoteis(Resource):
    def get(self):
        return {'hoteis': hoteis}
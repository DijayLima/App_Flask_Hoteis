from flask_restful import Resource, reqparse

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

class Hotel(Resource):
    def get(self, hotel_id):
        for hotel in hoteis:
            if hotel['hotel_id'] == hotel_id:
                return hotel
        
        return {'Message': 'Hotel not found.'}, 404
    
    def post(self, hotel_id):
        arguments = reqparse.RequestParser()
        arguments.add_argument('name')
        arguments.add_argument('estrela')
        arguments.add_argument('diaria')
        arguments.add_argument('cidade')
        
        dados = arguments.parse_args()
        
        novo_hotel = {
            'hotel_id': hotel_id,
            'name': dados['name'],
            'estrela': dados['estrela'],
            'diaria': dados['diaria'],
            'cidade': dados['cidade']
        }
        
        hoteis.append(novo_hotel)
        
        return novo_hotel

    def put(self):
        pass
    
    def delete(self):
        pass
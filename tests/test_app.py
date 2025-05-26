import unittest
from unittest.mock import patch
from app import create_app

class TestArtGalleryApp(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_home_page(self):
        # Mock the API response
        mock_response = {
            'data': [
                {
                    'id': 1,
                    'title': 'Test Artwork',
                    'artist_display': 'Test Artist',
                    'date_display': '2000',
                    'image_id': 'test-image-id'
                }
            ],
            'pagination': {
                'total_pages': 100,
                'current_page': 1
            }
        }

        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = mock_response
            
            response = self.client.get('/')
            
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Test Artwork', response.data)
            self.assertIn(b'Test Artist', response.data)

    def test_artwork_detail(self):
        # Mock the API response
        mock_response = {
            'data': {
                'id': 1,
                'title': 'Test Artwork Detail',
                'artist_display': 'Test Artist',
                'date_display': '2000',
                'medium_display': 'Oil on canvas',
                'dimensions': '100 × 100 cm',
                'credit_line': 'Test Credit',
                'description': 'Test Description',
                'image_id': 'test-image-id'
            }
        }

        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = mock_response
            
            response = self.client.get('/artwork/1')
            
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Test Artwork Detail', response.data)
            self.assertIn(b'Test Artist', response.data)
            self.assertIn(b'Oil on canvas', response.data)

    def test_search_with_results(self):
        # Mock the API response
        mock_response = {
            'data': [
                {
                    'id': 1,
                    'title': 'Search Result Artwork',
                    'artist_display': 'Search Artist',
                    'date_display': '2000',
                    'image_id': 'test-image-id'
                }
            ],
            'pagination': {
                'total_pages': 1,
                'current_page': 1
            }
        }

        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = mock_response
            
            response = self.client.get('/search?q=test')
            
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Search Result Artwork', response.data)
            self.assertIn(b'Search Artist', response.data)

    def test_search_no_query(self):
        response = self.client.get('/search')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Enter a search term to find artworks', response.data)

    def test_api_error_handling(self):
        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 500
            
            response = self.client.get('/')
            
            self.assertEqual(response.status_code, 500)
            self.assertIn(b'Error fetching artworks', response.data)

    def test_artwork_not_found(self):
        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 404
            
            response = self.client.get('/artwork/999999')
            
            self.assertEqual(response.status_code, 404)
            self.assertIn(b'Artwork not found', response.data)


if __name__ == '__main__':
    unittest.main() 
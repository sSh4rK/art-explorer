
from flask import Blueprint, render_template, request
import requests

main = Blueprint('main', __name__)

API_BASE_URL = "https://api.artic.edu/api/v1"

@main.route('/')
def index():
    # Get artworks from the API
    page = request.args.get('page', 1, type=int)
    limit = 12  # Number of artworks per page
    
    response = requests.get(
        f"{API_BASE_URL}/artworks",
        params={
            'page': page,
            'limit': limit,
            'fields': 'id,title,image_id,artist_display,date_display'
        }
    )
    
    if response.status_code == 200:
        data = response.json()
        artworks = data['data']
        pagination = data['pagination']
        
        # Add image URLs to the artworks
        for artwork in artworks:
            if artwork.get('image_id'):
                artwork['image_url'] = f"https://www.artic.edu/iiif/2/{artwork['image_id']}/full/400,/0/default.jpg"
            else:
                artwork['image_url'] = None
                
        return render_template(
            'index.html',
            artworks=artworks,
            pagination=pagination,
            current_page=page
        )
    else:
        return "Error fetching artworks", 500

@main.route('/artwork/<int:artwork_id>')
def artwork_detail(artwork_id):
    response = requests.get(
        f"{API_BASE_URL}/artworks/{artwork_id}",
        params={
            'fields': 'id,title,image_id,artist_display,date_display,medium_display,dimensions,credit_line,description'
        }
    )
    
    if response.status_code == 200:
        artwork = response.json()['data']
        
        if artwork.get('image_id'):
            artwork['image_url'] = f"https://www.artic.edu/iiif/2/{artwork['image_id']}/full/800,/0/default.jpg"
        else:
            artwork['image_url'] = None
            
        return render_template('artwork.html', artwork=artwork)
    else:
        return "Artwork not found", 404

@main.route('/search')
def search():
    query = request.args.get('q', '')
    page = request.args.get('page', 1, type=int)
    limit = 12
    
    if not query:
        return render_template('search.html', artworks=None, query=None)
    
    response = requests.get(
        f"{API_BASE_URL}/artworks/search",
        params={
            'q': query,
            'page': page,
            'limit': limit,
            'fields': 'id,title,image_id,artist_display,date_display'
        }
    )
    
    if response.status_code == 200:
        data = response.json()
        artworks = data['data']
        pagination = data['pagination']
        
        for artwork in artworks:
            if artwork.get('image_id'):
                artwork['image_url'] = f"https://www.artic.edu/iiif/2/{artwork['image_id']}/full/400,/0/default.jpg"
            else:
                artwork['image_url'] = None
                
        return render_template(
            'search.html',
            artworks=artworks,
            pagination=pagination,
            current_page=page,
            query=query
        )
    else:
        return "Error performing search", 500
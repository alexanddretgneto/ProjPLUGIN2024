from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page

import requests
from bs4 import BeautifulSoup
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@cache_page(60 * 15)  # Cache por 15 minutos
def noticias(request):
    urls = [
        'https://g1.globo.com/',
        'https://g1.globo.com/index/feed/pagina-2.ghtml',
        'https://g1.globo.com/index/feed/pagina-4.ghtml'
        # Substitua 'https://example.com' pela sua segunda URL
    ]
    headlines = []
    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            posts = soup.find_all('div', class_='feed-post-body')
            for post in posts:
                # Encontra o título e o link da notícia
                link_element = post.find('a', class_='feed-post-link')
                title = link_element.text.strip() if link_element else ''
                link = link_element['href'] if link_element and 'href' in link_element.attrs else ''
                
                # Encontra o link da imagem da notícia
                image_element = post.find('img', class_='bstn-fd-picture-image')
                image_url = image_element['src'] if image_element else ''
                
                # Adiciona o título, URL da imagem e link da notícia à lista de manchetes
                if title and image_url and link:
                    headline = {'title': title, 'image_url': image_url, 'link': link}
                    headlines.append(headline)
        else:
            headlines = []

    return render(request, 'noticias/noticias.html', {'headlines': headlines})


import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
from django.shortcuts import render
from urllib.parse import urlparse

def detalhes_noticia(request, url):
    # Corrigir a formatação da URL se necessário
    parsed_url = urlparse(url)
    if not parsed_url.scheme:
        url = 'http://' + url
    elif not parsed_url.netloc:
        url = parsed_url.scheme + '://' + url

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Encontrar o elemento que contém o título da notícia
        title_element = soup.find('h1', class_='content-head__title', itemprop='headline')
        title = title_element.text.strip() if title_element else 'Título da Notícia Não Encontrado'
        # Encontrar todos os elementos <p> dentro da classe content-text__container
        paragraphs = soup.find_all('p', class_='content-text__container')
        # Extrair o texto de cada parágrafo
        paragraphs_text = [p.get_text() for p in paragraphs]
        # Passar o título, a URL e os parágrafos para o template
        context = {'title': title, 'paragraphs': paragraphs_text}
        return render(request, 'noticias/detalhes_noticia.html', context)
    else:
        return HttpResponse('Erro ao acessar a página da notícia.')

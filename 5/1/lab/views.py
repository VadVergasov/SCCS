from django.shortcuts import render
from django.http.request import HttpRequest

from museum_api.models import Article
from museum_api.serializers import ArticleSerializer


def index(request: HttpRequest):
    queryset = Article.objects.last()
    article: Article = ArticleSerializer(queryset, many=False).data
    return render(
        request,
        "index.html",
        {
            "article_name": article["name"],
            "article_id": article["id"],
        },
    )


def get_article(request: HttpRequest, id: int):
    article = Article.objects.get(id=id)
    return render(
        request,
        "generated.html",
        {
            "title": article.name,
            "content": f"<h1>{article.name}</h1><p>{article.content}</p>",
        },
    )

from django.shortcuts import render, redirect
from django.http.request import HttpRequest

from museum_api.models import Article, Review
from museum_api.serializers import ArticleSerializer, ReviewSerializer


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


def privacy(request: HttpRequest):
    return render(
        request,
        "generated.html",
        {
            "title": "Политика конфиденциальности",
            "content": """<h1>Политика конфиденциальности</h1><article>Политика конфиденциальности сайта музея\r\n\r\n<q>Мы, Музей, рады приветствовать вас на нашем сайте.</q> Наша главная цель - предоставление информации о музее и его коллекциях, а также обеспечение удобства и безопасности для наших посетителей.\r\n\r\nДля этого мы придерживаемся политики конфиденциальности, которая гарантирует защиту ваших личных данных и информации, которую вы предоставляете на нашем сайте.\r\n\r\n<ol><li>Мы не собираем и не храним личную информацию, такую как имя, адрес, номер телефона или электронную почту, если вы не предоставляете ее добровольно. Если вы решите поделиться такой информацией, мы используем ее только для связи с вами и для предоставления вам информации о музеях и мероприятиях.</li>\r\n\r\n<li>Мы также не передаем вашу информацию третьим лицам без вашего согласия, за исключением случаев, когда это требуется по закону. Например, мы можем передавать информацию о посетителях, которые совершили покупку или оплатили услугу на нашем сайте, нашим поставщикам и партнерам для выполнения транзакций и предоставления услуг.</li>\r\n\r\n<li>Если вы хотите отказаться от получения рекламы и информации от нас, вы можете связаться с нами через форму обратной связи на нашем сайте или по электронной почте, указав, что вы хотите прекратить получение сообщений.</li>\r\n\r\n</ol>Спасибо за ваше доверие и посещение нашего сайта. Мы ценим вашу конфиденциальность и гарантируем, что ваши данные будут использоваться только в соответствии с этой политикой конфиденциальности.</article>""",
        },
    )


def about(request: HttpRequest):
    reviews = Review.objects.all()
    serialized = ReviewSerializer(reviews, many=True)
    return render(request, "about.html", {"reviews": serialized.data})


def promos(request: HttpRequest):
    return render(request, "promos.html")


def articles(request: HttpRequest):
    articles = Article.objects.all()
    serialized = ArticleSerializer(articles, many=True)
    return render(request, "articles.html", {"articles": serialized.data})


def contacts(request: HttpRequest):
    return render(request, "contacts.html")


def get_article(request: HttpRequest, id: int):
    article = Article.objects.get(id=id)
    return render(
        request,
        "generated.html",
        {
            "title": article.name,
            "content": f"<h1>{article.name}</h1><article style=\"column-count: 2; column-gap: 20px; \">\n\r{article.content}</article>",
        },
    )


def submit_review(request: HttpRequest):
    review = Review.objects.create(
        title=request.POST.get("title"), content=request.POST.get("review"), mark=request.POST.get("rating")
    )
    return redirect("index")

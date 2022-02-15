# hachathon22
проект комиков

база данных - первая версия, которую скинули в тг (она слишком тяжелая, не смогли приврепить)

## Примечание.
Позже мы обнаружили, что ссылки, которые выдает программа, значительно отличаются от желаемых. В них нет тех продуктов, которые мы искали. Скорее всего, это связано с тем, что рецепты из базы данных и с сайта отличаются. 
Например, вот ингредиенты для Арбулястры: 1 - из дата сета, 2 - с сайта.
![изображение](https://user-images.githubusercontent.com/72147905/154064157-8937fea3-7452-4678-afa5-8e9296d21454.png)
![изображение](https://user-images.githubusercontent.com/72147905/154064184-8a223352-9210-48e9-bc23-2245c0aec448.png)

## Игры с прорицанием
Мы решили попробовать научить модель Word2Vec работать оракулом: получив введенный пользователем ингредиент, она предлагает список других, встречающихся в рецептах вместе с ним чаще всего. Кроме того, наша модель почти всегда умеет находить лишний ингредиент из предложенного списка.

Мы обучали ее на материале текста, собранного из списка ингредиентов для каждого конкретного блюда (одна строка - один список).
![изображение](https://user-images.githubusercontent.com/72147905/154069244-d94111af-58fc-4bb4-a21b-f44699d67e2e.png)

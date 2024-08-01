from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    # comment_set = 클래스 이름따라 자동 생성('클래스이름_set' / 눈에 보이지는 않지만) - 포린키 연결 가능하게 쌍방향

class Comment(models.Model):
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE) # 부모가 지워지면 자식 요소도 지워주세요
    # article_id = 장고가 자동으로 생성해주는 컬럼 (숫자만 - 아티클과 둘 중 하나 선택)
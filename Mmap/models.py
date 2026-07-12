from django.db import models
from django.contrib.auth.models import User


class MindMap(models.Model):
    # マップのタイトル
    title = models.CharField(max_length=255, default="新規マップ")

    # 誰のマップか（ユーザーが削除されたらマップも削除する設定）
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mindmaps', null=True, blank=True)

    # マインドマップのツリー構造全体をJSON形式で保存
    data = models.JSONField(default=dict, blank=True)

    # 作成日時と更新日時（自動記録）
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title